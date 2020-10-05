# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:36:34 2020

@author: LuisVillegas
"""

from app.ObtenerDatos import blueprint
from flask import render_template, redirect, url_for
from app.ObtenerDatos import OrganizarLogs

@blueprint.route('/equipo')
def equipo():
    logs = OrganizarLogs.leer_directorios()
    return render_template('equipos.html', len=len(logs), logs=logs, title="Obtener Datos")

@blueprint.route('/equipo/<log_id>')
def Getdatos(log_id):
    Equipo = log_id
    datos = OrganizarLogs.crear_plot(log_id)
    return render_template('graficas.html', length=len(datos), Equipo=Equipo,title="Datos de Equipo")

@blueprint.route('/prueba')
def pruebas():
    return render_template('prueba.html')