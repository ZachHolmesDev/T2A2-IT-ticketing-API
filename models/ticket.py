from main import db 


# class Ticket(db.Model):
#     __tablename__ = 'tickets'
#     id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title       = db.Column(db.String)
#     description = db.Column(db.Text)
#     priority    = db.Column(db.String)
#     status      = db.Column(db.String)
#     created_at  = db.Column(db.DateTime)
#     updated_at  = db.Column(db.DateTime)
#     created_by  = db.Column(db.Integer, db.ForeignKey('users.id'))
#     assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))

#     # relationship
#     comments = db.relationship("Comment", backref="tickets")
    
class Ticket(db.Model):
    __tablename__ = 'tickets'
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title       = db.Column(db.String)
    description = db.Column(db.Text)
    priority    = db.Column(db.String)
    status      = db.Column(db.String)
    created_at  = db.Column(db.DateTime)
    updated_at  = db.Column(db.DateTime)

    created_by  = db.Column(db.Integer, db.ForeignKey('users.id'))
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))

    # relationship
    # ticket_comments = db.relationship(
    #                         "Comments", 
    #                         back_populates="comment_ticket")
    # ticket_creator  = db.relationship(
    #                         "User",
    #                           foreign_keys=[created_by])
    # ticket_assignee = db.relationship(
    #                         "User", 
    #                         foreign_keys=[assigned_to])


    # created_by_user = db.relationship("User", foreign_keys=[created_by], backref="created_tickets")
    # assigned_to_user = db.relationship("User", foreign_keys=[assigned_to], backref="assigned_tickets")
    # ticket_comments = db.relationship("Comment", backref="ticket")
    
    # created_by_user = db.relationship("User", foreign_keys=[created_by], back_populates="created_tickets")
    # assigned_to_user = db.relationship("User", foreign_keys=[assigned_to], back_populates="assigned_tickets")
    # ticket_comments = db.relationship("Comment", back_populates="ticket")