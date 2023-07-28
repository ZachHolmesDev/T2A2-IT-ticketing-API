from main import db 


class TicketCategories(db.Model):
    __tablename__ = 'ticket_categories'
    ticket_id   = db.Column(db.Integer, db.ForeignKey('tickets.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)

    # relationship
    ticket = db.relationship("Ticket", backref="ticket_categories")