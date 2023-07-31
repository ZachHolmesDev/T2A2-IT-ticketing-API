from datetime import timedelta
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import create_access_token
from marshmallow.exceptions import ValidationError
from main import db, bcrypt

# models and schemas
from models.comment import Comment
from schemas.user_schema import user_schema, users_schema
from schemas.comment_schema import comment_schema, comments_schema

comments_bp = Blueprint("comments", __name__, url_prefix="/comments")


# GET /tickets: Retrieves a list of all tickets
@comments_bp.get("/")
def get_all_comments(): 
    stmt     = db.select(Comment)
    comments = db.session.scalars(stmt)
    return comments_schema.dump(comments)


# GET /tickets/<id>: Retrieves a specific ticket by its ID
@comments_bp.get('/<int:id>')
def get_user_by_id(id): 
    stmt    = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    return comment_schema.dump(comment)


@comments_bp.get('/<int:id>/comments')
def get_user_and_comments_by_id(id): 
    stmt = db.select(Comment).filter_by(id=id)
    user = db.session.scalar(stmt)
    return user_schema.dump(user)


