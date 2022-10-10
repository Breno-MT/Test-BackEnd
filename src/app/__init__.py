from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from src.app.config import app_config


DB = SQLAlchemy()
MA = Marshmallow()


def create_app(enviroment):

    app = Flask(__name__)

    app.config.from_object(app_config[enviroment])

    DB.init_app(app)
    MA.init_app(app)

    Migrate(app=app, db=DB, directory="./src/app/migrations")

    CORS(app)

    app.config["Access-Control-Allow-Origin "] = "*"
    app.config["Access-Control-Allow-Headers"] = "Content-Type"

    return app


