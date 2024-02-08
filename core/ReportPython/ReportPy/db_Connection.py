import pyodbc
import pandas as pd

from variables import *
from df_Constructor import *
from xls_path import *
from query import *
from functions import *
#--------------------------------------------------------#

#--------------------------------------------------------#

def consulta_query(query):
    print('Genera coneccion con BD')
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    data = cursor.execute(query,(fechaConsultaDesde, fechaConsultaHasta))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    print('Cierra coneccion con BD')
    return results


def consulta_query_tarjeta(query):
    print('Genera coneccion con BD')
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    data = cursor.execute(query,(fechaConsultaHasta))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    print('Cierra coneccion con BD')
    return results


def consulta_query_retop(query):
    print('Genera coneccion con BD')
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    fechaDesde = datetime.strptime(fechaConsultaDesde, "%Y%m%d")
    fechaDesde = fechaDesde - timedelta(days=6)
    fechaDesde = fechaDesde.strftime("%Y%m%d")

    data = cursor.execute(query,(fechaDesde, fechaConsultaHasta, finanPresRetop))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    print('Cierra coneccion con BD')
    return results


def consulta_query_compra(query):
    print('Genera coneccion con BD')
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    fechaDesde = datetime.strptime(fechaConsultaDesde, "%Y%m%d")
    fechaDesde = fechaDesde - timedelta(days=6)
    fechaDesde = fechaDesde.strftime("%Y%m%d")

    data = cursor.execute(query,(fechaDesde, fechaConsultaHasta, finanPresCompraA))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    print('Cierra coneccion con BD')
    return results


def consulta_query_promotora(query):
    print('Genera coneccion con BD')
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    fechaDesde = datetime.strptime(fechaConsultaDesde, "%Y%m%d")
    fechaDesde = fechaDesde - timedelta(days=6)
    fechaDesde = fechaDesde.strftime("%Y%m%d")

    data = cursor.execute(query,(fechaDesde, fechaConsultaHasta, finanPresPromo))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    print('Cierra coneccion con BD')
    return results


def consulta_query_sodexo(query):
    print('Genera coneccion con BD')
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    fechaDesde = datetime.strptime(fechaConsultaDesde, "%Y%m%d")
    fechaDesde = fechaDesde - timedelta(days=6)
    fechaDesde = fechaDesde.strftime("%Y%m%d")

    data = cursor.execute(query,(fechaDesde, fechaConsultaHasta, finanPresSodexo))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    print('Cierra coneccion con BD')
    return results


def consulta_query_manuales(query):
    print('Genera coneccion con BD')
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    day = today.day
    month = today.month
    year = today.year 

    if month == 1 and day == 3:
        day = fechaPresManual[3]
        month = 12
        year = year -1

    elif day_num == 3:
        day = fechaPresManual[3]
        month = today.month -1
    elif day_num == 11:
        day = fechaPresManual[0]
        month = today.month 
    elif day_num == 18:
        day = fechaPresManual[1]
        month = today.month 
    elif day_num == 26:
        day = fechaPresManual[2]
        month = today.month 

    fechaDesde = datetime(year, month, day)

    fecha = datetime.strptime(fechaConsultaHasta, "%Y%m%d")
    fechaHasta = fecha - timedelta(days=1)
    fechaHasta = fechaHasta.strftime("%Y%m%d")
    fechaDesde = fechaDesde.strftime("%Y%m%d")

    data = cursor.execute(query,(fechaDesde, fechaHasta, *finanManuales))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    print('Cierra coneccion con BD')
    return results



def consulta_query_CD(query):
    print('Genera coneccion con BD')
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    fecha = datetime.strptime(fechaConsultaHasta, "%Y%m%d")
    fechaDesde = fecha - timedelta(days=9)
    fechaHasta = fecha - timedelta(days=3)
    fechaHasta = fechaHasta.strftime("%Y%m%d")
    fechaDesde = fechaDesde.strftime("%Y%m%d")

    data = cursor.execute(query,(fechaDesde, fechaHasta, finanPresCD))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    print('Cierra coneccion con BD')
    return results


def consulta_query_cierre_tarjeta(query):
    print('Genera coneccion con BD')
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    data = cursor.execute(query,(fechaConsultaHasta))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    print('Cierra coneccion con BD')
    return results


#--------------------------------------------------------#

def consulta_query_promo(query, promo):
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    data = cursor.execute(query,(fechaDesdePromo, fechaHastaPromo, promo))
    results = cursor.fetchall()

    data = pd.DataFrame(results)

    connection.close()
    return results



def consulta_query_pres(query):
    today = fecha.strftime('%A')

    if today == 'Monday':
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        diaDesde = fecha - timedelta(days=7)
        diaDesde = diaDesde.strftime("%Y%m%d")

        diaHasta = fecha - timedelta(days=1)
        diaHasta = diaHasta.strftime("%Y%m%d")

        data = cursor.execute(query,(diaDesde, diaHasta))
        results = cursor.fetchall()

        data = pd.DataFrame(results)

        connection.close()
        return results
    else:
        print('Hoy no es lunes')

