# app.py


import os

from flask import Flask

from extensions import (
    bcrypt,
    cors,
    db,
    jwt,
    admin
)

from covey.models import *

from covey.views.auth import auth_blueprint
from covey.views.ping import ping_blueprint


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}})
    bcrypt.init_app(app)
    jwt.init_app(app)
    if os.getenv("FLASK_ENV") == "development":
        admin.init_app(app)

    # register routes
    app.register_blueprint(ping_blueprint)
    app.register_blueprint(auth_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
