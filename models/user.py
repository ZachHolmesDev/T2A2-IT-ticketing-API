from main import db 


# class User(db.Model):
#     __tablename__ = 'users'
    
#     id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name          = db.Column(db.String)
#     email         = db.Column(db.String, unique=True, nullable=False)
#     password_hash = db.Column(db.String)
#     role_id       = db.Column(db.Integer, db.ForeignKey('role.id'))

#     # relationships
#     created_tickets  = db.relationship("Ticket", foreign_keys='Ticket.created_by', backref="creator")
#     assigned_tickets = db.relationship("Ticket", foreign_keys='Ticket.assigned_to', backref="assignee")
#     comments         = db.relationship("Comment",foreign_keys='', backref="")
    
    
class User(db.Model):
    __tablename__ = 'users'
    
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name          = db.Column(db.String)
    email         = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String)

    role_id       = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    
    # created_tickets = db.relationship("Ticket",
    #                                   foreign_keys='Ticket.created_by', 
    #                                   back_populates="created_by_user", 
    #                                   cascade='all, delete'
    #                                   )
    # assigned_tickets = db.relationship("Ticket",
    #                                    foreign_keys='Ticket.assigned_to', 
    #                                    back_populates="assigned_to_user", 
    #                                    cascade='all, delete'
    #                                    )
    

    created_comments = db.relationship('Comment', 
                                        back_populates='user', 
                                        cascade='all, delete')
