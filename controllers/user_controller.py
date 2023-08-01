from datetime import timedelta
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError
from main import db, bcrypt

# models and schemas
from models.user import User
from schemas.user_schema import user_schema, users_schema
from schemas.comment_schema import comment_schema, comments_schema

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

# POST /users: Creates a new user

# PUT/PATCH /users/<id>: Updates a specific user by its ID

# DELETE /users/<id>: Deletes a specific user by its ID
