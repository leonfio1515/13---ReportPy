from logic_Query import *
from variables import day_name, day_num, fechaPresManual
#-----------------------------------------------------------------------#

#-----------------------------------------------------------------------#

def process_generate():
    promo_cumple()
    fp_control()
    desc_doble()
    control_tarjetas()
    control_cierre_tarjetas()

    if day_num in fechaPresManual:
        pres_manuales()
    if day_name == 'Monday':
        pres_retop()
        pres_compra_A()
        pres_promotora()    
        pres_creditos_D()    
        pres_sodexo()

process_generate()

