from datetime import datetime
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError
from main import db 
from helpers import check_permissions_wrap, jwt_required_and_user_exists, jwt_required_and_user_exists

# models and schemas
from models.ticket import Ticket
from schemas.ticket_schema import ticket_schema, tickets_schema
from schemas.comment_schema import comment_schema, comments_schema

tickets_bp = Blueprint("tickets", __name__, url_prefix="/tickets")


# GET /tickets: Retrieves a list of all tickets
"""
retrieves a list of all tickets from the database and returns them as
a JSON response.

:return: 
    a list of all tickets in the database.
"""
@tickets_bp.get("/")
@jwt_required_and_user_exists
def get_all_tickets():
    tickets_query = db.select(Ticket)
    tickets       = db.session.scalars(tickets_query)
    return tickets_schema.dump(tickets)
    
    
# GET /tickets/<id>: Retrieves a specific ticket by its ID
"""
retrieves a specific ticket by its ID and returns it as a response.

:param id: 
    The `id` parameter is the unique identifier of the ticket that you want to retrieve
:return: 
    the ticket with the specified ID if it exists. If the ticket does not exist, it returns a
    JSON response with a message indicating that the ticket was not found and a status code of 404.
"""
@tickets_bp.get('/<int:id>')
@jwt_required_and_user_exists
def get_ticket_by_id(id): 
    stmt   = db.select(Ticket).filter_by(id=id)
    ticket = db.session.scalar(stmt)
    if not ticket: 
        return {"message": f"ticket with id: {id} not found"}, 404
    return ticket_schema.dump(ticket)


# POST /tickets: Creates a new ticket
"""
creates a new ticket by validating the data, creating a new ticket instance, and
adding it to the database.

:return: 
    The code is returning a JSON response with the newly created ticket data and a status code
    of 201 (indicating a successful creation). If there is a validation error, it returns a JSON
    response with an error message and the validation error messages. If there is an integrity error
(such as a duplicate entry), it returns a JSON response with an error message.
"""
@tickets_bp.post("/")
@jwt_required_and_user_exists
def create_ticket():
    try:
        # Get the JSON data from the request
        ticket_request = request.get_json()
        # Validate the data using the ticket schema
        ticket_data = ticket_schema.load(ticket_request, partial=True)

        # Create a new ticket instance using the validated data
        new_ticket = Ticket(
            title          = ticket_data.get('title'),
            description    = ticket_data.get('description'),
            created_at     = datetime.now(),
            priority       = ticket_data.get('priority'),
            status         = 'incoming',
            created_by_id  = get_jwt_identity(),
            )
        # Add and commit the new ticket to the database
        db.session.add(new_ticket)
        db.session.commit()

        return ticket_schema.dump(new_ticket), 201
    except ValidationError as err:
        return {"message": "Validation Error", "errors": err.messages}, 400
    except IntegrityError as err:
        return {"message": "Integrity Error, Bad request, NOTE to create a ticket you must provide Title, description and priority.  Check error for more info", "errors": f'{err.orig}'}, 400


# PUT/PATCH /tickets/<id>: Updates a specific ticket by its ID
"""
updates a specific ticket by its ID, allowing for partial updates of
the ticket fields.

:param id: 
    The ID of the ticket that needs to be updated
:param user_role: 
    The `user_role` parameter represents the role of the user making the request. It
    is used to check the permissions of the user before updating the ticket
:return: 
    the updated ticket object in JSON format if the ticket is found and updated successfully.
    If the ticket is not found, it returns an error message with a 404 status code. If there is a
    validation error with the JSON data, it returns a validation error message with a 400 status code.
    If the user does not have the necessary permissions to update the ticket, it returns an unauthorized
"""
@tickets_bp.put('/<int:id>')
@tickets_bp.patch('/<int:id>')
@jwt_required_and_user_exists
@check_permissions_wrap
def update_ticket(id, user_role):
    try:
        # Get the JSON data and validate it with the schema, allowing for partial updates
        ticket_request = request.get_json()
        ticket_data    = ticket_schema.load(ticket_request, partial=True)

        # Query the ticket
        stmt   = db.select(Ticket).filter_by(id=id)
        ticket = db.session.scalar(stmt)
        
        if not ticket:
            return {'error': f'Ticket not found with id {id}'}, 404

        if ticket:
            # Check permissions
            if str(ticket.created_by_id) != get_jwt_identity() and user_role.can_edit_all == False:
                return {'error': 'Unauthorized'}, 403
            
            # Update only the fields that are provided
            ticket.title       = ticket_data.get('title')       or ticket.title
            ticket.description = ticket_data.get('description') or ticket.description
            ticket.priority    = ticket_data.get('priority')    or ticket.priority

            if user_role.can_edit_all == True or user_role.can_manage_tickets == True:
                ticket.status         = ticket_data.get('status') or ticket.status
                ticket.assigned_to_id = ticket_data.get('assigned_to_user_id') or ticket.assigned_to_id
            ticket.updated_at  = datetime.now()

            db.session.commit()
            return ticket_schema.dump(ticket)
    except ValidationError as err:
        # Validation error, return 400 response
        return {"message": "Validation Error", "errors": err.messages}, 400



# DELETE /tickets/<id>: Deletes a specific ticket by its ID
    """
    The `delete_ticket` function deletes a specific ticket by its ID, after checking if the user has the
    necessary permissions.
    
    :param id:
        The `id` parameter represents the ID of the ticket that needs to be deleted
    :param user_role: 
        The `user_role` parameter represents the role of the user making the request. It
        is used to check if the user has the necessary permissions to delete the ticket
    :return: 
        a JSON response with a message indicating the result of the deletion. If the ticket is
        successfully deleted, the message will be "Ticket deleted" with a status code of 200. If the ticket
        is not found, the message will be "Ticket not found" with a status code of 404. If the user is
        unauthorized to delete the ticket, the message will be "Unauthorized
    """
@tickets_bp.delete('/<int:id>')
@jwt_required_and_user_exists
@check_permissions_wrap
def delete_ticket(id, user_role):
    stmt   = db.select(Ticket).filter_by(id=id)
    ticket = db.session.scalar(stmt)
    if not ticket:
        return {"message": "Ticket not found"}, 404

    user_id = get_jwt_identity()
    if user_id != str(ticket.created_by_id) and user_role.can_delete_all == False:
        return {"message": "Unauthorized"}, 403

    db.session.delete(ticket)
    db.session.commit()
    return {"message": "Ticket deleted"}, 200
