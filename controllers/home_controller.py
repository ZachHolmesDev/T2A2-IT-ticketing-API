from flask import Blueprint, jsonify

home = Blueprint("home", __name__)


@home.get("/")
def hello():
    return { 'message': 'hello world'}
