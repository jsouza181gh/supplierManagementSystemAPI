from flask import Flask
from controllers import blueprints
from database import createDataBase

app = Flask(__name__)

for blueprint in blueprints:
    app.register_blueprint(blueprint)

if __name__ == "__main__":
    createDataBase()
    app.run(debug=True)