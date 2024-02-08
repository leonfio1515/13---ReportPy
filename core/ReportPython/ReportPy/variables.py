from datetime import datetime, timedelta
from pathlib import Path
import os

#---------------------------------------------------#

directory = 'usuario'

#----------------DIRECTORIO DJANGO--------------------------#
project_directory = os.path.dirname(os.path.abspath(__file__))  
project_directory = os.path.dirname(project_directory)

#---------------MAIL CONFIG--------------------------#
adressee_cajas = ['example@mail.com', 'example2@mail.com']

adressee_cierre_tarj = ['example4@mail.com', 'example3@mail.com']

# adressee_cierre_tarj = ['lfiorentino@stadium.com.uy']

# adressee_cajas = ['lfiorentino@stadium.com.uy']

#---------------------------------------------------#
today = datetime.now()
day_name = today.strftime("%A")
day_num = today.day


fecha = datetime.today().date()
fechahoy = fecha.strftime("%Y%m%d")

fechaDesdeCumple = fecha - timedelta(days=7)
fechaConsulta = fecha - timedelta(days=1)

año_actual = fechaConsulta.year

fechaConsultaHasta = fechaConsulta.strftime("%Y%m%d")
fechaConsultaDesde = fechaConsulta.strftime("%Y%m%d")

fechaDesdeCumple = fechaDesdeCumple.strftime("%Y%m%d")

#---------------------------------------------------#

fechaDesde = fecha - timedelta(days=1)
fechaHasta = fecha - timedelta(days=7)

fechaDesde = fechaDesde.strftime("%d-%m")
fechaHasta = fechaHasta.strftime("%d-%m")
#---------------------------------------------------#


#-------------- FECHAS CIBER -----------------------#

fechaDesdeCiber = '20231106'
fechaHastaCiber = '20231120'

fechaPresManual = (3, 11, 18, 26)

tiendasCiber = (71, 75)
marcasCiber = (21, 53, 54, 57, 74, 127, 129, 131, 142, 143, 144, 193, 201)


finanTarj = (3, 4, 6, 7, 9, 13, 18, 19, 23, 27, 28, 36, 40)

finanPresRetop = 5
finanPresCompraA = 11
finanPresPromo = 42
finanPresCD = 35
finanPresSodexo = 38
finanManuales = (6003, 6004, 6006, 6007, 6009, 6018, 6027, 6028, 6036)

#---------------------------------------------------#

fechaDesdePromo = '20231116'
fechaHastaPromo = '20231119'

#---------------------------------------------------#


rute_path = f'c:\\Users\\{directory}\\Desktop\\ReportPy'
output_folder = Path(rute_path) / f'Reportes {fechaConsulta}'


#---------------------------------------------------#

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
data10 = []
data11 = []
data12 = []
data13 = []
data14 = []
data15 = []
data16 = []
data17 = []
data18 = []
data19 = []
data20 = []
data21 = []
data22 = []
data23 = []
data24 = []
data25 = []
data26 = []



