from datetime import datetime
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError
from main import db 
from helpers import check_permissions_wrap

# models and schemas
from models.ticket import Ticket
from schemas.ticket_schema import ticket_schema, tickets_schema
from schemas.comment_schema import comment_schema, comments_schema

tickets_bp = Blueprint("tickets", __name__, url_prefix="/tickets")


# GET /tickets: Retrieves a list of all tickets
@tickets_bp.get("/")
@jwt_required()
def get_all_tickets():
    tickets_query = db.select(Ticket)
    tickets       = db.session.scalars(tickets_query)
    return tickets_schema.dump(tickets)
    
    
# GET /tickets/<id>: Retrieves a specific ticket by its ID
@tickets_bp.get('/<int:id>')
@jwt_required()
def get_ticket_by_id(id): 
    stmt   = db.select(Ticket).filter_by(id=id)
    ticket = db.session.scalar(stmt)
    if not ticket: 
        return {"message": f"ticket with id: {id} not found"}, 404
    return ticket_schema.dump(ticket)


# POST /tickets: Creates a new ticket
@tickets_bp.post("/")
@jwt_required()
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
        # Validation error, return 400 response
        return {"message": "Validation Error", "errors": err.messages}, 400



# PUT/PATCH /tickets/<id>: Updates a specific ticket by its ID
@tickets_bp.put('/<int:id>')
@tickets_bp.patch('/<int:id>')
@jwt_required()
@check_permissions_wrap
def update_ticket(id, user_role):
    try:
        # Get the JSON data and validate it with the schema, allowing for partial updates
        ticket_request = request.get_json()
        ticket_data    = ticket_schema.load(ticket_request, partial=True)

        # Query the ticket
        stmt   = db.select(Ticket).filter_by(id=id)
        ticket = db.session.scalar(stmt)

        if ticket:
            # Check permissions
            if str(ticket.created_by_id) != get_jwt_identity() and user_role.can_edit_all == False:
                return {'error': 'Unauthorized'}, 403
            
            # Update only the fields that are provided
            ticket.title       = ticket_data.get('title', ticket.title)
            ticket.description = ticket_data.get('description', ticket.description)
            ticket.priority    = ticket_data.get('priority', ticket.priority)
            ticket.status      = ticket_data.get('status', ticket.status)
            ticket.updated_at  = datetime.now()

            db.session.commit()
            return ticket_schema.dump(ticket)
        else:
            return {'error': f'Ticket not found with id {id}'}, 404
    except ValidationError as err:
        # Validation error, return 400 response
        return {"message": "Validation Error", "errors": err.messages}, 400



# DELETE /tickets/<id>: Deletes a specific ticket by its ID
@tickets_bp.delete('/<int:id>')
@jwt_required()
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
