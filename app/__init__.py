from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)
    
    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
