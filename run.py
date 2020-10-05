# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:28:15 2020

@author: LuisVillegas
"""
from flask_migrate import Migrate
from os import environ
from sys import exit

from config import config_dict
from app import create_app, db

get_config_mode = environ.get('APP_CONFIG_MODE', 'Debug')

try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit("Error: Invalid APP_CONFIG_MODE environment variable entry.")

app = create_app(config_mode)
Migrate(app, db)

if __name__ == "__main__":
    app.run()
