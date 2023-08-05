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
"""
retrieves a list of all comments from the database and returns them
as a JSON response.

:return: 
    a list of all comments.
"""
@comments_bp.get("/")
@jwt_required_and_user_exists
def get_all_comments(): 
    stmt     = db.select(Comment)
    comments = db.session.scalars(stmt)
    return comments_schema.dump(comments)


# GET /comments/<id>: Retrieves a specific comment by its ID
"""
The function retrieves a specific comment by its ID and returns it as a JSON response.

:param id: 
    The `id` parameter is the unique identifier of the comment that you want to retrieve. It
    is used to filter the comments and retrieve the specific comment with the matching ID
:return: 
    The specific comment with the given ID is being returned.
"""
@comments_bp.get('/<int:id>')
@jwt_required_and_user_exists
def get_comment_by_id(id): 
    stmt    = db.select(Comment).filter_by(id=id)
    comment = db.session.scalar(stmt)
    return comment_schema.dump(comment)



# POST /comments: Creates a new comment
"""
creates a new comment by validating the request data, creating a new comment instance,
and adding it to the database.

:return: 
    The code is returning the newly created comment in JSON format along with a status code of
    201 (indicating a successful creation). If there is a validation error, it returns a JSON response
    with a message indicating the validation error and the specific validation errors. If there is an
    integrity error (such as missing required fields), it returns a JSON response with a message
    indicating the integrity error and the specific error
"""
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
    except IntegrityError as err:
        return {"message": "IntegrityError make sure your include a ticket id and content", "errors": f'{err.orig}'}, 400


# PUT/PATCH /comments/<id>: Updates a specific comment by its ID
"""
The `update_comment` function updates a specific comment by its ID, allowing the user to change the
comment's content and link it to a different ticket if they have the necessary permissions.

:param id: 
    The ID of the comment that needs to be updated
:param user_role: 
    The `user_role` parameter represents the role of the user making the request. It
    is used to check the user's permissions and determine if they are authorized to update the comment
:return: 
    The code is returning the updated comment in JSON format if the update is successful. If
    there is a validation error, it returns a 400 response with the validation error messages. If there
    is an integrity error, it returns a 400 response with an error message indicating that a ticket ID
    and content should be included.
"""
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
        return {"message": "IntegrityError make sure your include a ticket id and content", "errors": f'{err.orig}'}, 400


# DELETE /comments/<id>: Deletes a specific comment by its ID
"""
deletes a specific comment by its ID, after checking if the user has
the necessary permissions.

:param id: 
    The `id` parameter represents the ID of the comment that needs to be deleted
:param user_role: 
    The `user_role` parameter represents the role of the user making the request. It
    is used to check if the user has the necessary permissions to delete the comment
:return: 
    a JSON response with a message indicating the result of the deletion. If the comment is
    successfully deleted, the message will be "Comment deleted" with a status code of 200. If the
    comment is not found, the message will be "Comment not found" with a status code of 404. If the user
    is unauthorized to delete the comment, the message will be "Unauthorized
"""
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
