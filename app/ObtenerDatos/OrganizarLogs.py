# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:41:24 2020

@author: LuisVillegas
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import config

CORE_DIR = config.Config.CORE_DIR
LOGS_DIR = config.Config.LOGS_DIR

def leer_directorios():
    """
    Crea una lista de de los archivos .log que se encuentran en un directorio
    """
    logDir= LOGS_DIR
    lista_logs = os.listdir(logDir)
    logs = []
    id_logs = []
    for archivo in lista_logs:
        if os.path.isfile(os.path.join(logDir, archivo)) and archivo.endswith('.log'):
            logs.append(archivo)
            arg = archivo.strip('speedtest-').split('.')
            id_logs.append(arg[0])
            pd_logs = pd.Series(logs, index= id_logs)
    return pd_logs


def crear_plot(log_id):
    """
    Devuelve la lista de datos leidos de  leer_archivos al controlador 
    """
    logDir = LOGS_DIR
    archivo = ("speedtest-{}.log".format(log_id))
    log = logDir+archivo
    df = leer_archivo(log)
    return df, 

def leer_archivo(log):
    """
    Lee el archivo .log que se sea llamado desde el controlador 
    """
    df = pd.io.parsers.read_csv(
        log,
        names='date time ping download upload'.split(),
        header=None,
        sep=r'\s+',
        parse_dates={'timestamp': [0, 1]},
        date_parser=formato_fecha,
        na_values=['TEST', 'FAILED'],
        )
    return df


def crear_grafica(df, log_id):
    """Crea la grafica con los datos devueltos de crear_plot"""
    plt.plot(df['timestamp'], df['download'], 'b-')
    plt.grid(True)
    plt.show()



def formato_fecha(d,t):
    """
    Organiza los datos de date y time en un formato leible para la leer_archivo
    """
    dt = d + " " + t
    return datetime.strptime(dt, '%Y-%m-%d %H:%M')


def max_download(datos):
    """
    Carga los datos en un intervalo de tiempo para devolver el maximo numero alcalzado
    """
    datos = datos
    return datos.max()


def min_donwload():
    """
    Carga los datos de un intervalo de tiempo para devolver el minimo numero alcanzado
    """
    pass


def avg_download():
    """
    Carla de datos de un intervalo de tiepo para devolver el averaje de numeros alcanzado
    """
    pass


def cat_horas_productivas():
    """
    Retorna el numero de horas productivas o conectadas a internet en un periodo de tiempo
    """
    pass


def anl_horas_productivas():
    """
    retorna el periodo del dia donde puede haber mayor productividad o mejor coneccion a internet
    """
    pass


if __name__ == "__main__":
    crear_plot('STIGDD01')
    