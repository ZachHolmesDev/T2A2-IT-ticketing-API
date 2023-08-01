from main import db 


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title       = db.Column(db.String)
    description = db.Column(db.Text)
    created_at  = db.Column(db.DateTime)
    updated_at  = db.Column(db.DateTime)
    priority    = db.Column(db.String)
    status      = db.Column(db.String)
    # foeiren keys
    created_by_id  = db.Column(db.Integer, db.ForeignKey('users.id'))
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # relationship
    created_by_user = db.relationship('User',
                                       foreign_keys   = 'Ticket.created_by_id',
                                       back_populates = 'created_tickets')
    assigned_to_user= db.relationship("User", 
                                      foreign_keys   = 'Ticket.assigned_to_id',
                                      back_populates = "assigned_tickets")
    comments        = db.relationship("Comment", 
                                       back_populates = "ticket",
                                       cascade        = 'all, delete')
    
    