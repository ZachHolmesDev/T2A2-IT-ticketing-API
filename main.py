from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError


db     = SQLAlchemy()
ma     = Marshmallow()
bcrypt = Bcrypt()
jwt    = JWTManager()


def create_app():
    app = Flask(__name__)
   
    app.config.from_object("config.app_config")
    app.json.sort_keys = False

    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404
    
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"message": "Validation Error", "errors": err.messages}, 400
   
    @app.errorhandler(IntegrityError)
    def integrity_error(err):
        return {"message": "Integrity Error",'error': f'{err.orig}'}, 400
    
    @app.errorhandler(500)
    def server_error(err):
        return {'error': str(err)}, 500

    @app.errorhandler(Exception)
    def exception_error(err):
        return {'error': str(err)}, 400
       
        
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    from commands import db_commands
    app.register_blueprint(db_commands)

    return app
