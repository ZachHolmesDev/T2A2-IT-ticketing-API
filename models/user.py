from main import db 


class User(db.Model):
    __tablename__ = 'users'
    
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name          = db.Column(db.String)
    email         = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    role_id       = db.Column(db.Integer, db.ForeignKey('role.id'))

    # relationships
    created_tickets  = db.relationship("Ticket", foreign_keys='Ticket.created_by', backref="creator")
    assigned_tickets = db.relationship("Ticket", foreign_keys='Ticket.assigned_to', backref="assignee")
    comments         = db.relationship("Comment", backref="user")