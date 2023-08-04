from main import db 


class Role(db.Model): 
    __tablename__ = 'role'
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name     = db.Column(db.String)
    # permissions
    can_view_all   = db.Column(db.Boolean)
    can_delete_all = db.Column(db.Boolean)
    can_edit_all   = db.Column(db.Boolean)
    can_manage_users  = db.Column(db.Boolean)
    can_manage_tickets  = db.Column(db.Boolean)
    can_assign_tickets  = db.Column(db.Boolean)

    # relationship
    users = db.relationship("User", backref="user_role")