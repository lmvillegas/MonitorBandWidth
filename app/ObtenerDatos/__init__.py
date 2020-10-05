# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:28:15 2020

@author: LuisVillegas
"""

from flask import Blueprint

blueprint = Blueprint(
    'ObtenerDatos_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
    )