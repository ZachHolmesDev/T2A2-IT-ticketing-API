from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask import Blueprint, abort, jsonify, request
from main import db, bcrypt

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
    
    # check if user exists
    # pass
    
    # if user dosent already create new user
# needs err hnadling
    new_user_role = db.session.query(Role).filter_by(
                    role_name=new_user_request.get('role')
                    ).first().id

    # new_user_role =  db.session.execute(db.select(Role).filter_by(
    #                  role_name=new_user_request.get('role'))
    #                  ).scalar_one()
    # need better name for var 
    user_to_add = User(name          = new_user_request.get('name'),
                       email         = new_user_request.get('email'),
                       password_hash = bcrypt.generate_password_hash(new_user_request.get('password')).decode('utf-8'),
                       # onty an admin should be able to create new admins 
                       # techs can make other techs ?
                       # need to search for role by name and get the ID od that role ?
                       role_id = new_user_role
                    )
    
    # Add and Commit the new user to the database
    db.session.add(user_to_add)
    db.session.commit()
    
    return user_schema.dump(user_to_add), 201

# Login:
# POST /login: Checks the user credentials and returns a JWT.
@auth.post('/login')
def login():
    pass
