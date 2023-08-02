import functools
from flask_jwt_extended import get_jwt_identity
from flask import request
from main import db
from models.user import User
from models.role import Role

# wrapper or function ??
# function 
def check_permissions_func(permission):
    # get the user 
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)

    user_role = db.session.query(Role).filter_by(id=user.role_id)
# wrapper
def check_permissions_wrap(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        stmt    = db.select(User).filter_by(id=user_id)
        user    = db.session.scalar(stmt)
        
        user_role = db.session.query(Role).filter_by(id=user.role_id).first()
        
        if request.endpoint == 'auth.auth_register_admin':
            if user_role.can_manage_users == False:
                return {'verboten': str(404)}, 403
            # else:
            #     return
        


        kwargs['user_role'] = user_role # Add user_role to kwargs
        return fn(*args, **kwargs) # Call the original function and return its result
    return wrapper    
    
    

def general_error_handler():
    pass