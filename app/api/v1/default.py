from flask import Blueprint, request, jsonify, json, redirect

api_default = Blueprint('default', __name__)


@api_default.route('/', methods=['GET'])
def default():
    """Logs in up user"""
    return redirect('/apidocs')
