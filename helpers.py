import functools
from flask_jwt_extended import get_jwt_identity
from flask import request
from main import db
from models.user import User
from models.role import Role


def check_permissions_wrap(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        # get the user from id 
        user_id = get_jwt_identity()
        stmt    = db.select(User).filter_by(id=user_id)
        user    = db.session.scalar(stmt)
        # Check if user is None
        # important for edge case of a user with a valid token carrying a user id that is no longer in the db
        if user is None:
            return {'error': 'User not found'}, 404
        # get the role of the user, includes all the permissions 
        user_role = db.session.query(Role).filter_by(id=user.role_id).first()

        kwargs['user_role'] = user_role # Add user_role to kwargs
        return fn(*args, **kwargs) # Call the original function and return its result
    return wrapper    
    
    

def general_error_handler():
    pass