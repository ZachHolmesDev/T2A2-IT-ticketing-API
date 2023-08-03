from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required
from flask import Blueprint, abort, jsonify, request
from main import db, bcrypt
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from helpers import check_permissions_wrap

from models.user import User
from models.role import Role
from schemas.user_schema import user_schema
from schemas.role_schema import role_schema

auth = Blueprint("auth", __name__, url_prefix="/auth")

# debug
@auth.get('/whatisaendpoint')
def anendpoint():
    return {'message': f'{request.endpoint}'}


def register_user(**kwargs):
    # get body data
    new_user_request = request.get_json()
    
    # not getting not null violations for empty string so this will do for now 
    # im sure thers an issue with it so need to find a better solution
    if new_user_request.get('email') == '':
        return { 'error': 'Email address cant be empty' }, 400
    try:
                                                    # new_user_role = db.session.execute(Role).filter_by(
                                                    #                                 role_name=new_user_request.get('role')
                                                    #                                 ).scalar_one()
        # get the id of the role by name 
        # cant figure out new request above to the right so using legacy for now
        if request.endpoint == 'auth.auth_register_admin':
            new_user_role = db.session.query(Role).filter_by(
                            role_name=new_user_request.get('role').lower()
                            ).first().id
        else:
            new_user_role = db.session.query(Role).filter_by(
                            role_name='user'
                            ).first().id   
    except AttributeError:
        # can be handled better i think
        return {'error': f'Role: {new_user_request.get("role")} invalid'}
    
    
    user_to_add = User(name          = new_user_request.get('name'),
                       email         = new_user_request.get('email'),
                       password_hash = bcrypt.generate_password_hash(new_user_request.get('password')).decode('utf-8'),
                       role_id       = new_user_role
                       # only an admin should be able to create new admins and techs can make other techs ?
                    )
    try:
        # Add and Commit the new user to the database
        db.session.add(user_to_add)
        db.session.commit()
        return user_schema.dump(user_to_add), 201
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return { 'error': 'Email address already in use' }, 409


# Registration:
# POST /register: Protected endpoint that allows users with the permission can_manage_users to creates all users.
@auth.post('/register/admin')
@jwt_required()
@check_permissions_wrap
def auth_register_admin(**kwargs):
    return register_user(**kwargs)


# POST /register: Unprotected endpoint that allows anyonone to creates a new user.
@auth.post('/register')
def auth_register(**kwargs):
    return register_user(**kwargs)

# Login:
# POST /login: Checks the user credentials and returns a JWT.
@auth.post('/login')
def login():
    login_request = request.get_json()

    stmt = db.select(User).filter_by(email=login_request.get('email'))
    user = db.session.scalar(stmt)
    
    if user and bcrypt.check_password_hash(user.password_hash, login_request.get('password')):
        
        # create token with identity
        token = create_access_token(identity=str(user.id),
                                    expires_delta=timedelta(days=1))
        
        return {'message':f'welcome {user.name} here is your token', 
                'token'  : token }
    else:
        return { 'error': 'Invalid email or password' }, 401