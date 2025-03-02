from flask import Blueprint,jsonify, request
import logging 


users_bp = Blueprint("users", __name__)

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


users = ["Alice", "Bob", "Charlie"]

@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@users_bp.route('/users', methods=['POST'])
def add_user():  
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Missing 'username' in request"}), 400
    
    username = data['username']
    logger.info(f"a user has been added!")
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    users.append(username)
    return jsonify(users)