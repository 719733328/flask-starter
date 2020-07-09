from flask import Flask
from config import config


def create_app(config_name):
    from . import models, routes, services, extensions, utils
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    extensions.init_app(app)
    models.init_app(app)
    routes.init_app(app)
    services.init_app(app)
    utils.init_app(app)
    return app
