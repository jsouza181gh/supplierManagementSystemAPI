import os
from dotenv import load_dotenv
from controllers import blueprints
from database import createDataBase
from flask import Flask, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import timedelta
from waitress import serve

load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_EXPIRE_TIME = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES"))

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=JWT_EXPIRE_TIME)
jwt = JWTManager(app)

for blueprint in blueprints:
    app.register_blueprint(blueprint)

@app.errorhandler(Exception)
def handle_exceptions(e):
    if hasattr(e, "status_code"):
        return jsonify({"error": str(e)}), e.status_code
    
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    createDataBase()
    serve(app, host="0.0.0.0", port=5000)