from main import db 


class Categories(db.Model):
    __tablename__ = 'categories'
    id             = db.Column(db.Integer, primary_key=True, autoincrement=True)
    categorie_name = db.Column(db.String)

    # relationship
    ticket_categories = db.relationship("TicketCategories", backref="categories")