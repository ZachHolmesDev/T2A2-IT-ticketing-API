from main import db 


# class Comment(db.Model):
#     __tablename__ = 'comment'
#     id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     content    = db.Column(db.Text)
#     created_at = db.Column(db.DateTime)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     ticket_id  = db.Column(db.Integer, db.ForeignKey('tickets.id'))


class Comment(db.Model):
    __tablename__ = 'comment'
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content    = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    user_id   = db.Column(db.Integer, db.ForeignKey('users.id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))
    # user = db.relationship("User", backref="comments")

    # user_id = db.relationship("User", back_populates="created_comments", cascade='all')
    
    ticket = db.relationship("Ticket", 
                             back_populates="comments")
    user   = db.relationship('User', 
                             back_populates='created_comments')