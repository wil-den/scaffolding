from flask import Flask
from flask_cors import CORS

from .main import bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    CORS(app)
    return app

def run_app():
    app = create_app()
    app.run()
