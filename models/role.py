from main import db 


class Role(db.Model): 
    __tablename__ = 'role'
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name     = db.Column(db.String)
    can_view_all  = db.Column(db.Boolean)
    can_manage    = db.Column(db.Boolean)
    can_action    = db.Column(db.Boolean)

    # relationship
    users = db.relationship("User", backref="role")
