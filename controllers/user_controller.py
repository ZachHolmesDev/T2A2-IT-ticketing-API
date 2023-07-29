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


# GET /tickets: Retrieves a list of all tickets
@users_bp.get("/")
def get_all_users():
    users_query = db.select(User)
    users = db.session.scalars(users_query)
    return users_schema.dump(users)
    
    
    


# GET /tickets/<id>: Retrieves a specific ticket by its ID

# POST /tickets: Creates a new ticket

# PUT /tickets/<id>: Updates a specific ticket by its ID

# DELETE /tickets/<id>: Deletes a specific ticket by its ID
