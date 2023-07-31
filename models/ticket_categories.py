from main import db 


# class TicketCategories(db.Model):
#     __tablename__ = 'ticket_categories'
#     # ticket_id   = db.Column(db.Integer, db.ForeignKey('tickets.id'), primary_key=True)
#     # category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)
#     ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
#     category_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     # relationship
#     ticket = db.relationship("Ticket", backref="ticket_categories")

