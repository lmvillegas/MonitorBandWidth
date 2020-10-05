# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:52:35 2020

@author: LuisVillegas
"""

from flask import Blueprint

blueprint = Blueprint(
    'base_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
    )
