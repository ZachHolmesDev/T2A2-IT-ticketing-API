from main import db 

    
class User(db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name          = db.Column(db.String)
    email         = db.Column(db.String, nullable=False, unique=True )
    password_hash = db.Column(db.String)

    role_id       = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    

    created_tickets  = db.relationship("Ticket",
                                      foreign_keys   = 'Ticket.created_by_id',
                                      back_populates = "created_by_user",
                                      cascade        = 'all, delete')
    assigned_tickets = db.relationship("Ticket",
                                       foreign_keys   = 'Ticket.assigned_to_id',
                                       back_populates = "assigned_to_user",
                                       cascade        = 'all, delete')
    created_comments = db.relationship('Comment', 
                                        back_populates = 'user',
                                        cascade        = 'all, delete')
