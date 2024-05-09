from flask import Flask, render_template, url_for, redirect, request
from datetime import timedelta
import os
from .database import db, Bus
from .bus_api import bus


def create_app():

    app = Flask(__name__)

    # load the instance config, if it exists, when not testing
    app.config.from_mapping(
                SECRET_KEY='dev',
                SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL'),
                SQLALCHEMY_TRACK_MODIFICATIONS=False)
    #postgresql://myhobbymanager_user:6bOLgaG5y4pGRqkPxAQFWf51YQfzVj2v@dpg-couhtk8l6cac73co4sag-a.singapore-postgres.render.com/myhobbymanager

    #db.app = application
    db.init_app(app)

    app.register_blueprint(stats)

