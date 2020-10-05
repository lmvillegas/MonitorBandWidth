# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:28:15 2020

@author: LuisVillegas
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from importlib import import_module
from logging import basicConfig,DEBUG,getLogger,StreamHandler

db = SQLAlchemy()


# login_manager = LoginManager()


def register_blueprints(app):
    for module_name in ('base', 'ObtenerDatos', ):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_logs(app):
    try:
        basicConfig(filename = 'CORE/log/error.log', level = DEBUG)
        logger = getLogger(__name__)
        logger.addHandler(StreamHandler())
    except:
        pass


def create_app(config, selenium=False):
    app = Flask(__name__, static_folder = 'base/static')
    app.config.from_object(config)
    if selenium:
        app.config['LOGIN_DISABLED'] = True
    # register_extensions(app)
    register_blueprints(app)
    # configure_database(app)
    configure_logs(app)
    # apply_themes(app)
    return app
