from datetime import timedelta
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import create_access_token
from marshmallow.exceptions import ValidationError
from main import db, bcrypt

# models and schemas 
from models.user import User
from schemas.user_schema import user_schema, users_schema

users = Blueprint("users", __name__, url_prefix="/users")

