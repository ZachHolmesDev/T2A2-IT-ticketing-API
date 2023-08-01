from datetime import timedelta
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow.exceptions import ValidationError
from main import db, bcrypt

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
    return ticket_schema.dump(ticket)


# POST /tickets: Creates a new ticket

# PUT/PATCH /tickets/<id>: Updates a specific ticket by its ID

# DELETE /tickets/<id>: Deletes a specific ticket by its ID
