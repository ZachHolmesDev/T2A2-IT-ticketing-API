from main import db 


class Comment(db.Model):
    __tablename__ = 'comment'
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content    = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    user_id   = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'), nullable=False)

    
    ticket = db.relationship("Ticket", 
                             back_populates="comments")
    user   = db.relationship('User', 
                             back_populates='created_comments')