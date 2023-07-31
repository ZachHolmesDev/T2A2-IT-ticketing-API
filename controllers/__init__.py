from controllers.home_controller import home
from controllers.auth_controller import auth
from controllers.user_controller import users_bp
from controllers.ticket_controler import tickets_bp
from controllers.comment_controller import comments_bp


registerable_controllers = [
    home,
    auth,
    users_bp,
    tickets_bp,
    comments_bp
]
