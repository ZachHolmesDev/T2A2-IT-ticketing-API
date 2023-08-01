from datetime import timedelta
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError
from main import db, bcrypt

# models and schemas
from models.comment import Comment
from schemas.user_schema import user_schema, users_schema
from schemas.comment_schema import comment_schema, comments_schema

comments_bp = Blueprint("comments", __name__, url_prefix="/comments")


# GET /comments: Retrieves a list of all comments
@comments_bp.get("/")
@jwt_required()
def get_all_comments(): 
    stmt     = db.select(Comment)
    comments = db.session.scalars(stmt)
    return comments_schema.dump(comments)


# GET /comments/<id>: Retrieves a specific comment by its ID
@comments_bp.get('/<int:id>')
@jwt_required()
def get_user_by_id(id): 
    stmt    = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    return comment_schema.dump(comment)



# POST /comments: Creates a new comment

# PUT/PATCH /comments/<id>: Updates a specific comment by its ID

# DELETE /comments/<id>: Deletes a specific comment by its ID
