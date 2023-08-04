from datetime import timedelta
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError
from main import db, bcrypt
from helpers import check_permissions_wrap


# models and schemas
from models.user import User
from models.role import Role
from schemas.user_schema import user_schema, users_schema

users_bp = Blueprint("users", __name__, url_prefix="/users")


# GET /users: Retrieves a list of all users
"""
retrieves a list of all users from the database and returns it as a
JSON response.
"""
@users_bp.get("/")
@jwt_required()
def get_all_users():
    stmt  = db.select(User)
    users = db.session.scalars(stmt)
    return users_schema.dump(users)


# GET /users/<id>: Retrieves a specific user by its ID
"""
retrieves a specific user by its ID and returns the user data in JSON format.

:param id: 
    The `id` parameter is the unique identifier of the user that we want to retrieve. It is
    used to filter the user records in the database and retrieve the specific user with the matching ID
:return: 
    The specific user with the given ID is being returned.
"""
@users_bp.get('/<int:id>')
@jwt_required()
def get_user_by_id(id): 
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    return user_schema.dump(user)

# PUT/PATCH /users/<id>: Updates a specific user by its ID
"""
This function updates a specific user by its ID, checking for permissions and validating the user
data.

:param id: 
    The `id` parameter represents the ID of the user that needs to be updated
:param user_role: 
    The `user_role` parameter represents the role of the user making the request. It
    is used to check the permissions of the user and determine if they are authorized to update the user
    with the given ID
:return: 
    the updated user data in JSON format.
"""
@users_bp.put('/<int:id>')
@users_bp.patch('/<int:id>')
@jwt_required()
@check_permissions_wrap
def update_user(id, user_role):
    try:
        #  Get the JSON data and validate it with the schema
        # partial=True for only updating certain feilds
        user_data = user_schema.load(request.get_json(), partial=True)
        
        # find the chosen user
        stmt = db.select(User).filter_by(id=id)
        user = db.session.scalar(stmt)
        
        # check user exists
        if not user:
            return {'error': f'User not found with id {id}'}, 404
        
        # check permissions
        if str(user.id) != get_jwt_identity() and user_role.can_manage_users == False:
            return {'error': 'Unauthorized'}, 403
        
        # change fields of chosen user
        user.name = user_data.get('name') or user.name
        user.email = user_data.get('email') or user.email
        # if user give a password in the request hash and store hash
        if user_data.get('password'):
            user.password_hash = bcrypt.generate_password_hash(user_data.get('password')).decode('utf-8')
        # if permission can change role else role is the same
        if user_role.can_manage_users and user_data.get('role'):
            # finds id of role by selecting using the role name provided by the user
            new_role_id = db.session.query(Role).filter_by(
                role_name=user_data.get('role').lower()).first().id
            user.role_id = new_role_id

        db.session.commit()
        return user_schema.dump(user)
    except ValidationError as err:
        return {"message": "Validation Error", "errors": err.messages}, 400
        

# DELETE /users/<id>: Deletes a specific user by its ID
@users_bp.delete('/<int:id>')
@jwt_required()
@check_permissions_wrap
def delete_user(id, user_role):
    if user_role.can_manage_users == False:
        return {"message": "Forbidden"}, 403

    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)

    if not user:
        return {"message": "User not found"}, 404

    db.session.delete(user)
    db.session.commit()
    return {"message": "User deleted"}, 200

