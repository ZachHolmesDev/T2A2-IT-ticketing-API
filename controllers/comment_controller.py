from datetime import datetime
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_identity
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError
from main import db
from helpers import check_permissions_wrap, jwt_required_and_user_exists, jwt_required_and_user_exists



# models and schemas
from models.comment import Comment
from schemas.comment_schema import comment_schema, comments_schema

comments_bp = Blueprint("comments", __name__, url_prefix="/comments")


# GET /comments: Retrieves a list of all comments
@comments_bp.get("/")
@jwt_required_and_user_exists
def get_all_comments(): 
    stmt     = db.select(Comment)
    comments = db.session.scalars(stmt)
    return comments_schema.dump(comments)


# GET /comments/<id>: Retrieves a specific comment by its ID
@comments_bp.get('/<int:id>')
@jwt_required_and_user_exists
def get_comment_by_id(id): 
    stmt    = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    return comment_schema.dump(comment)



# POST /comments: Creates a new comment
@comments_bp.post("/")
@jwt_required_and_user_exists
def create_comment():
    try:
        # Get the JSON data from the request
        comment_request = request.get_json()
        # Validate the data using the comment schema
        comment_data = comment_schema.load(comment_request, partial=True)

        # Create a new comment instance using the validated data
        new_comment = Comment(
            ticket_id  = comment_data.get('ticket_id'),
            content    = comment_data.get('content'),
            created_at = datetime.now(),
            user_id    = get_jwt_identity()
        )
        # Add and commit the new comment to the database
        db.session.add(new_comment)
        db.session.commit()

        return comment_schema.dump(new_comment), 201
    except ValidationError as err:
        # Validation error, return 400 response
        return {"message": "Validation Error", "errors": err.messages}, 400
    # Might need to make more descriptive, but not sure about just saying no ticket in case of different integrity error
    except IntegrityError as err:
        return {"message": "IntegrityError, you may be trying to post a comment without a ticket ID", "errors": f'{err.orig}'}, 400


# PUT/PATCH /comments/<id>: Updates a specific comment by its ID
@comments_bp.put('/<int:id>')
@comments_bp.patch('/<int:id>')
@jwt_required_and_user_exists
@check_permissions_wrap
def update_comment(id, user_role):
    try:
        # Get the JSON data from the request
        comment_request = request.get_json()
        # Validate the data using the comment schema
        comment_data = comment_schema.load(comment_request, partial=True)

        # Find chosen comment
        stmt    = db.select(Comment).filter_by(id=id)
        comment = db.session.scalar(stmt)
        if not comment:
            return {'error': f'Comment not found with id {id}'}, 404

        # Check permissions
        if str(comment.user_id) != get_jwt_identity() and user_role.can_edit_all == False:
            return {'error': 'Unauthorized'}, 403
        
        # If permission, user can change the comment to link to a different ticket 
        if user_role.can_edit_all == True:
            comment.ticket_id = comment_data.get('ticket_id') or comment.ticket_id
        # change the content
        comment.content = comment_data.get('content') or comment.content
        
        db.session.commit()
        return comment_schema.dump(comment)
    except ValidationError as err:
        # Validation error, return 400 response
        return {"message": "Validation Error", "errors": err.messages}, 400
    except IntegrityError as err:
        return {"message": "IntegrityError", "errors": f'{err.orig}'}, 400


# DELETE /comments/<id>: Deletes a specific comment by its ID
@comments_bp.delete('/<int:id>')
@jwt_required_and_user_exists
@check_permissions_wrap
def delete_comment(id, user_role):
    stmt    = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    if not comment: 
        return {"message": "Comment not found"}, 404

    user_id = get_jwt_identity()
   
    if user_id != str(comment.user_id) and user_role.can_delete_all == False:
        return {"message": "Unauthorized"}, 403

    db.session.delete(comment)
    db.session.commit()
    return {"message": "Comment deleted"}, 200
