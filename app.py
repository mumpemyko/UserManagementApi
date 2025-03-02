from flask import Flask,jsonify
from blueprints.users.routes import users_bp
import logging

app = Flask(__name__)

app.register_blueprint(users_bp)
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@app.errorhandler(404)
def handler(e):
    logger.error(f"Error:{e}")
    return jsonify ({"error": "not found"}),404

if __name__ == '__main__':
    app.run(debug=True)