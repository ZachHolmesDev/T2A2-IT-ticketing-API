from main import db 


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
    comments = db.relationship("Comment", backref="tickets")