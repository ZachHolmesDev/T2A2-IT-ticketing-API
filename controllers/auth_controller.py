from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask import Blueprint, abort, jsonify, request
from main import db, bcrypt
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

from models.user import User
from models.role import Role
from schemas.user_schema import user_schema
from schemas.role_schema import role_schema


auth = Blueprint("auth", __name__, url_prefix="/auth")



# Registration:
# POST /register: Creates a new user and returns a JWT.
@auth.post('/register')
def auth_register():
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
        new_user_role = db.session.query(Role).filter_by(
                        role_name=new_user_request.get('role').lower()
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

# Login:
# POST /login: Checks the user credentials and returns a JWT.
@auth.post('/login')
def login():
    pass
