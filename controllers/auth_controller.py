from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required
from flask import Blueprint, abort, jsonify, request
from main import db, bcrypt
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from helpers import check_permissions_wrap
from marshmallow.exceptions import ValidationError


from models.user import User
from models.role import Role
from schemas.user_schema import user_schema
from schemas.role_schema import role_schema

auth = Blueprint("auth", __name__, url_prefix="/auth")

# debug
@auth.get('/whatisaendpoint')
def anendpoint():
    return {'message': f'{request.endpoint}'}


def register_user(user_role):
    """
    The `register_user` function registers a new user by validating the user data, determining the
    user's role, creating a new user instance, and adding it to the database.
    
    :param user_role: 
        The `user_role` parameter is the role of the user who is registering a new user.
        It is an object that contains information about the user's role, such as whether they have
        permission to manage users
    
    :return: 
        a response in the form of a JSON object. If the registration is successful, it returns the
        newly created user object along with a status code of 201 (created). 
        If there is a validation error, it returns an error message along with a status code of 400 (bad request). 
    """
    try:
        # Get the JSON data and validate it with the schema
        new_user_request = request.get_json()
        new_user_data    = user_schema.load(new_user_request)

        # Determine the role ID based on user role
        # 
        #   TODO
        # cant figure out new request above to the right so using legacy for now
        # 
        # Check if the user role is present and permission to manage users, 
        # and get the role name from the request if so
        if user_role and user_role.can_manage_users:
            role_name = new_user_data.get('role').lower()
            # Query the database for the role with the given name
            new_user_role = db.session.query(Role).filter_by(role_name=role_name).first()
            # If no such role exists, return an error
            if not new_user_role:
                return {'error': f'Role: {role_name} invalid'}, 400
        else:
            role_name = 'user'
            # Query the database for the default 'user' role
            new_user_role = db.session.query(Role).filter_by(role_name=role_name).first()
            # Optionally, handle the case if the default user role is not found

        # Create a new user instance
        new_user = User(
            name          = new_user_data.get('name'),
            email         = new_user_data.get('email'),
            password_hash = bcrypt.generate_password_hash(new_user_data.get('password')).decode('utf-8'),
            role_id       = new_user_role.id
        )
        # Add and commit the new user to the database and return created user
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201

    except ValidationError as err:
        # Validation error, return 400 response
        return {'error': err.messages}, 400
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {'error': 'Email address already in use'}, 409
    except Exception as e:
        return {'error': str(e)}, 500



# Registration:   #TODO Route now redundunt ?? due to proper permission imlementation 
                  # will change to make more sense if i get other stuff done in time
    """
    The function `auth_register_admin` is a protected endpoint that allows users with the permission
    `can_manage_users` to create all users.
    
    :param user_role: 
        The user_role parameter represents the role of the user making the request. It is
        used to check if the user has the necessary permission (can_manage_users) to create new users
    :return: 
        The function `auth_register_admin` is returning the result of the `register_user` function.
    """
# POST /register: Protected endpoint that allows users with the permission can_manage_users to creates all users.
@auth.post('/register/admin')
@jwt_required()
@check_permissions_wrap
def auth_register_admin(user_role):
    # check permission
    if user_role.can_manage_users == False:
        return {'Forbidden': str(403)}, 403
    return register_user(user_role)


# POST /register:
    """
    An unprotected endpoint that allows anyone to create a new user.
    
    :return: 
        The function `auth_register` is returning the result of the `register_user` function call
        with the `user_role` parameter set to `None`.
    """
@auth.post('/register')
def auth_register():
    return register_user(user_role= None)


# Login:
"""
The login function checks the user credentials, generates a JWT token if the credentials are valid,
and returns the token to the user.

:return: 
    If the user credentials are valid, the function will return a JSON object with a message
    and a token. The message will contain a welcome message with the user's name and the token will be a
    JWT (JSON Web Token) that can be used for authentication in subsequent requests.
"""
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
    

# Role: 
# POST /role: Allows an admin create new roles with whatever permissions required
@auth.post('/role')
def create_role():
    pass
# PATCH/PUT /role: Allows an admin to configure permissions as they require
@auth.put('/role')
@auth.patch('/role')
def edit_role():
    pass