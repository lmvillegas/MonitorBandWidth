# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 23:03:51 2020

@author: LuisVillegas
"""
from flask import render_template
from app.base import blueprint


@blueprint.route('/')
def route_default():
    return render_template('index.html')


@blueprint.route('/page_<error>')
def route_error(error):
    return render_template('errors/page_{}.html'.format(error))


# Errors


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('errors/page_403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('errors/page_500.html'), 500
