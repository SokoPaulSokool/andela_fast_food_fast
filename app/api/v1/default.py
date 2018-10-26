from flask import Blueprint, request, jsonify, json, redirect, send_from_directory, render_template, url_for

api_default = Blueprint('default', __name__)
api_static_js = Blueprint('serve_static_js', __name__)
api_static_html = Blueprint('serve_static_html', __name__)
api_static_css = Blueprint('serve_static_css', __name__)
api_static_img = Blueprint('serve_static_img', __name__)


@api_default.route('/', methods=['GET'])
def default():
    """Redire"""
    return render_template("index.html")


@api_static_html.route('/<path:filename>', methods=['GET'])
def serve_static_html(filename):
    return send_from_directory('../../../UI', filename)


@api_static_js.route('/js/<path:filename>', methods=['GET'])
def serve_static_js(filename):
    return send_from_directory('../../../UI/js', filename)


@api_static_css.route('/styles/<path:filename>', methods=['GET'])
def serve_static_css(filename):
    return send_from_directory('../../../UI/styles', filename)


@api_static_img.route('/img/<path:filename>', methods=['GET'])
def serve_static_img(filename):
    return send_from_directory('../../../UI/img', filename)
