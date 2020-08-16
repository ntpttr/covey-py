# covey/views/ping.py


from flask import Blueprint, jsonify


ping_blueprint = Blueprint('ping', __name__)


@ping_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "success", "message": "pong!"}), 200
