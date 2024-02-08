from variables import *
#-----------------------------------------------------------------------#

def create_df(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20,data21, data22, data23, data24):
    data = {
        'Fecha Doc':data4,
        'Suc':data1,
        'Caja':data2,
        'Tipo Doc':data11,
        'Numero Doc':data3,
        'Moneda':data12,
        'Total Doc':data5,
        'DescL %':data6,
        'DescG %':data7,
        'Precio Art':data9,
        'Forma Pago':data20,
        'Comentario':data10,
        'Cantidad':data16,
        'Art':data13,
        'Descripcion':data14,
        'Num Vend':data23,
        'Nombre Vend':data15,
        'CI Cliente':data17,
        'Nombre':data18,
        'Fecha Nac':data19,
        'Comentario':data24,
        'Precio Siva':data8,
        'DescL':data21,
        'DescG':data22,
    }

    return data


def create_df_tarj(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16):
    data_tarjetas = {
        'Fecha Doc':data4,
        'Suc':data1,
        'Caja':data2,
        'Tipo Doc':data8,
        'Numero Doc':data3,
        'Total Doc':data5,
        'DescL %':data6,
        'DescG %':data7,
        'Forma Pago':data11,
        'Nro Tarj':data12,
        'Autorizacion':data13,
        'Nro BIN':data14,
        'Cuotas':data15,
        'CI Cliente':data9,
        'Nombre':data10,
        'Forma de pago':data16,
    }

    return data_tarjetas


def create_df_tarj_cierre(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14):
    data_tarjetas = {
        'Fecha Doc':data4,
        'Suc':data1,
        'Caja':data2,
        'Tipo Doc':data6,
        'Numero Doc':data3,
        'Monto':data5,
        'Forma Pago':data7,
        'FP Tipo':data8,
        'Nro Tarj':data9,
        'Autorizacion':data10,
        'Nro BIN':data11,
        'Cuotas':data12,
        'Fecha Cierre':data13,
        'Hora':data14,
    }

    return data_tarjetas


def create_df_promo(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13):
    data_promo = {
        'Suc':data1,
        'Caja':data2,
        'Numero Doc':data3,
        'Fecha Doc':data4,
        'Tipo Doc':data5,
        'Monto':data6,
        'Forma Pago':data7,
        'Nro Tarjeta':data8,
        'Aut':data9,
        'ABIN':data10,
        'Cuota':data11,
        'Promocion':data12,
        'Comentario':data13,
    }


    return data_promo


def create_df_ciber(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13):
    data = {
        'Suc':data1,
        'Fecha':data3,
        'Num Doc':data4,
        'Tipo Doc':data5,
        'Articulo':data7,
        'Desc Art':data6,
        'Marca':data9,
        'Cantidad':data8,
        'Comentario':data2,
        'Precio s/iva':data10,
        'Precio':data11,
        'Desc G':data12,
        'Desc L':data13,
    }

    return data


def create_df_pres(data1, data2, data3, data4, data5, data6, data7):
    data_promo = {
        'Fecha Doc':data3,
        'Suc':data1,
        'Tipo Doc':data4,
        'Numero Doc':data2,
        'Forma Pago':data6,
        'FormaPago Num':data7,
        'Monto':data5,
    }

    return data_promo
