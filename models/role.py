from main import db 


class Role(db.Model): 
    __tablename__ = 'role'
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name     = db.Column(db.String, nullable=False)
    # permissions
    can_view_all       = db.Column(db.Boolean, nullable=False)
    can_delete_all     = db.Column(db.Boolean, nullable=False)
    can_edit_all       = db.Column(db.Boolean, nullable=False)
    can_manage_users   = db.Column(db.Boolean, nullable=False)
    can_manage_tickets = db.Column(db.Boolean, nullable=False)
    can_assign_tickets = db.Column(db.Boolean, nullable=False)

    # relationship
    users = db.relationship("User", backref="user_role")