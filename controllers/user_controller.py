from datetime import timedelta
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError
from main import db, bcrypt
from helpers import check_permissions_wrap


# models and schemas
from models.user import User
from schemas.user_schema import user_schema, users_schema

users_bp = Blueprint("users", __name__, url_prefix="/users")


# GET /users: Retrieves a list of all users
@users_bp.get("/")
@jwt_required()
def get_all_users():
    stmt  = db.select(User)
    users = db.session.scalars(stmt)
    return users_schema.dump(users)


# GET /users/<id>: Retrieves a specific user by its ID
@users_bp.get('/<int:id>')
@jwt_required()
def get_user_by_id(id): 
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    return user_schema.dump(user)

# PUT/PATCH /users/<id>: Updates a specific user by its ID
@users_bp.put('/<int:id>')
@users_bp.patch('/<int:id>')
@jwt_required()
@check_permissions_wrap
def update_user(id, user_role):
    if user_role.can_manage_users == False:
        return {"message": "Forbidden"}, 403

    user_data = request.get_json()
    stmt      = db.select(User).filter_by(id=id)
    user      = db.session.scalar(stmt)

    if user:
        user.name       = user_data.get('name', user.name)
        user.email      = user_data.get('email', user.email)
        user.email      = user_data.get('email', user.email)
        user.email      = user_data.get('email', user.email)
        # Additional fields go here

        db.session.commit()
        return user_schema.dump(user)
    else:
        return {'error': f'User not found with id {id}'}, 404


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