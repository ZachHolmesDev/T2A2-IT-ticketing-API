from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask import Blueprint, abort, jsonify, request
from main import db, bcrypt
from models.user import User


auth = Blueprint("auth", __name__, url_prefix="/auth")


