from flask import jsonify


class MessageResponse:
    @staticmethod
    def send(message, code):
        return jsonify({"message": message}), code
