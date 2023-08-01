from datetime import timedelta
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import create_access_token
from marshmallow.exceptions import ValidationError
from main import db, bcrypt

# models and schemas
from models.user import User
from schemas.user_schema import user_schema, users_schema
from schemas.comment_schema import comment_schema, comments_schema

users_bp = Blueprint("users", __name__, url_prefix="/users")


# GET /users: Retrieves a list of all users
@users_bp.get("/")
def get_all_users():
    stmt  = db.select(User)
    users = db.session.scalars(stmt)
    return users_schema.dump(users)


# GET /users/<id>: Retrieves a specific ticket by its ID
@users_bp.get('/<int:id>')
def get_user_by_id(id): 
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    return user_schema.dump(user)


# @users_bp.get('/<int:id>/comments')
# def get_user_and_comments_by_id(id): 
#     stmt = db.select(User).filter_by(id=id)
#     user = db.session.scalar(stmt)
#     return user_schema.dump(user)


