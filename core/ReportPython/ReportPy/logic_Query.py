from datetime import datetime
from db_Connection import *
from send_mail import *
import time
#-----------------------------------------------------------------------#
max_retries = 3

#-----------------------------------------------------------------------#

def promo_cumple():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Promo Cumple')

            query = query_generic
            name = 'Promo Cumple'

            results = consulta_query(query)

            try:
                print('Itera sobre el resultado')
                for row in results:
                    cont = 0

                    fechaNac = datetime.strptime(row[18], "%d-%m") 
                    fechaMes = fechaNac.month
                    fechaDia = fechaNac.day
                    fechaCumple = datetime(año_actual, fechaMes, fechaDia)
                    fechaCumple = fechaCumple.strftime("%Y%m%d")

                    hasta = fechaConsultaHasta
                    desde = fechaDesdeCumple

                    descG = row[5]
                    descL = row[6]

                    if desde <= fechaCumple <= hasta:
                        pass
                    elif descG == 25 or descL == 25:
                        iter_generic(row, cont)

            except Exception as e:
                print('Error al iterar los elementos', str(e))

            try:
                dataframe = create_df(
                data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23, data24
                )
            except Exception as e:
                print('Error al capturar data', str(e))

            try:
                XlsxConst(dataframe, fechaConsulta, name)
                clear_list()
            except Exception as e:
                print('Error al construir DF', str(e))

            print('Fin de proceso Promo Cumple - Ejecutado correctamente')
            break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
                print(str(e))
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
                print(str(e))
            else:
                print('Error:', e)
                break


def fp_control():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Control Forma de Pago')

            query = query_generic
            name = 'Forma de Pago'

            results = consulta_query(query)

            try:
                print('Itera sobre el resultado')
                for row in results:
                    cont = 0
                    descG = row[5]
                    descL = row[6]
                    formaPago = row[19]

                    if (formaPago in ['ITAU MILLAS LOCALES', 'CAMBIO DE MERCADERIA', 'Orden de Compra', 'Correo Uruguayo 2023'] and (descG > 9 or descL > 9)):
                        iter_generic(row, cont)
                    else:
                        pass
            except Exception as e:
                print('Error al iterar los elementos', str(e))

            try:
                dataframe = create_df(
                data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23, data24 
                )
            except Exception as e:
                print('Error al capturar data', str(e))

            try:
                XlsxConst(dataframe, fechaConsulta, name)
                clear_list()
            except Exception as e:
                print('Error al construir DF', str(e))


            print('Fin de proceso Formas de Pago - Ejecutado correctamente')
            break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


def desc_doble():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Control Descuento doble')

            query = query_generic
            name = 'Descuento Doble'

            results = consulta_query(query)

            try:
                print('Itera sobre el resultado')
                for row in results:
                    cont = 0
                    descG = row[5]
                    descL = row[6]

                    if descG > 0 and descL > 0:
                        iter_generic(row, cont)
                    else:
                        pass
            except Exception as e:
                print('Error al iterar los elementos', str(e))
                
            try:
                dataframe = create_df(
                data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20, data21, data22, data23, data24
                )
            except Exception as e:
                print('Error al capturar data', str(e))

            try:
                XlsxConst(dataframe, fechaConsulta, name)
                clear_list()
            except Exception as e:
                print('Error al construir DF', str(e))

            print('Fin de proceso Descuento doble - Ejecutado correctamente')
            break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


def control_tarjetas():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Control Tarjetas')
            query = query_tarj
            name = 'Cuotas Tarjetas'

            results = consulta_query_tarjeta(query)

            try:
                print('Itera sobre el resultado')
                for row in results:
                    cont = 0
                    financiera = row[15]
                    cuota = row[14]

                    if financiera in finanTarj:
                        if cuota == '12' and financiera in [27,7] or cuota == '14' and financiera in [4] or financiera in [45]:
                            pass
                        else:
                            iter_tarj(row, cont)
                    else:
                        pass
            except Exception as e:
                print('Error al iterar los elementos', str(e))
            
            try:
                dataframe = create_df_tarj(
                data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16
                )
            except Exception as e:
                print('Error al capturar data', str(e))

            try:        
                XlsxConst(dataframe, fechaConsulta, name)
                clear_list()
            except Exception as e:
                print('Error al construir DF', str(e))

            print('Fin de proceso Control cuotas - Ejecutado correctamente')
            break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


def pres_retop():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Presentacion Retop')
            query = query_pres
            name = 'Presentacion Retop'
            results = consulta_query_retop(query)

            if not results:
                print('No hay movimientos para el periodo')
                send_mail_clear(fechaConsulta, name)
                break
            else:
                try:
                    print('Itera sobre el resultado')

                    for row in results:
                        cont = 0
                        
                        iter_pres(row, cont)
                except Exception as e:
                    print('Error al iterar los elementos', str(e))
                
                try:
                    dataframe = create_df_pres(
                    data1, data2, data3, data4, data5, data6, data7
                    )
                except Exception as e:
                    print('Error al capturar data', str(e))
                
                try:
                    XlsxConst(dataframe, fechaConsulta, name)
                    clear_list()
                except Exception as e:
                    print('Error al construir DF', str(e))


                print('Fin de proceso Presentacion Retop - Ejecutado correctamente')
                break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


def pres_compra_A():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Presentacion Compra Agil')
            query = query_pres
            name = 'Presentacion Compra Agil'
            results = consulta_query_compra(query)

            if not results:
                print('No hay movimientos para el periodo')
                send_mail_clear(fechaConsulta, name)
                break
            else:
                try:
                    print('Itera sobre el resultado')

                    for row in results:
                        cont = 0
                        
                        iter_pres(row, cont)
                except Exception as e:
                    print('Error al iterar los elementos', str(e))
                
                try:
                    dataframe = create_df_pres(
                    data1, data2, data3, data4, data5, data6, data7, 
                    )
                except Exception as e:
                    print('Error al capturar data', str(e))
                
                try:
                    XlsxConst(dataframe, fechaConsulta, name)
                    clear_list()
                except Exception as e:
                    print('Error al construir DF', str(e))


                print('Fin de proceso Presentacion Compra Agil - Ejecutado correctamente')
                break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


def pres_promotora():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Presentacion Promotora')
            query = query_pres
            name = 'Presentacion Promotora'
            results = consulta_query_promotora(query)

            if not results:
                print('No hay movimientos para el periodo')
                send_mail_clear(fechaConsulta, name)
                break
            else:
                try:
                    print('Itera sobre el resultado')

                    for row in results:
                        cont = 0     
                        iter_pres(row, cont)

                except Exception as e:
                    print('Error al iterar los elementos', str(e))
                
                try:
                    dataframe = create_df_pres(
                    data1, data2, data3, data4, data5, data6, data7
                    )
                except Exception as e:
                    print('Error al capturar data', str(e))
                
                try:
                    XlsxConst(dataframe, fechaConsulta, name)
                    clear_list()
                except Exception as e:
                    print('Error al construir DF', str(e))


                print('Fin de proceso Presentacion Promotora - Ejecutado correctamente')
                break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


def pres_sodexo():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Presentacion Sodexo')
            query = query_pres
            name = 'Presentacion Sodexo'
            results = consulta_query_sodexo(query)

            if not results:
                print('No hay movimientos para el periodo')
                send_mail_clear(fechaConsulta, name)
                break
            else:
                try:
                    print('Itera sobre el resultado')
                    for row in results:
                        cont = 0     
                        iter_pres(row, cont)

                except Exception as e:
                    print('Error al iterar los elementos', str(e))
                
                try:
                    dataframe = create_df_pres(
                    data1, data2, data3, data4, data5, data6, data7
                    )
                except Exception as e:
                    print('Error al capturar data', str(e))
                
                try:
                    XlsxConst(dataframe, fechaConsulta, name)
                    clear_list()
                except Exception as e:
                    print('Error al construir DF', str(e))


                print('Fin de proceso Presentacion Sodexo - Ejecutado correctamente')
                break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


def pres_creditos_D():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Presentacion Creditos Directos')
            query = query_pres
            name = 'Presentacion Creditos Directos'
            results = consulta_query_CD(query)

            if not results:
                print('No hay movimientos para el periodo')
                send_mail_clear(fechaConsulta, name)
                break
            else:
                try:
                    print('Itera sobre el resultado')

                    for row in results:
                        cont = 0     
                        iter_pres(row, cont)

                except Exception as e:
                    print('Error al iterar los elementos', str(e))
                
                try:
                    dataframe = create_df_pres(
                    data1, data2, data3, data4, data5, data6, data7
                    )
                except Exception as e:
                    print('Error al capturar data', str(e))
                
                try:
                    XlsxConst(dataframe, fechaConsulta, name)
                    clear_list()
                except Exception as e:
                    print('Error al construir DF', str(e))


                print('Fin de proceso Presentacion Promotora - Ejecutado correctamente')
                break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


def pres_manuales():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Presentacion Manuales')
            query = query_pres_manuales
            name = 'Presentacion Manuales'
            results = consulta_query_manuales(query)

            if not results:
                print('No hay movimientos para el periodo')
                send_mail_clear(fechaConsulta, name)
                break
            else:
                try:
                    print('Itera sobre el resultado')

                    for row in results:
                        cont = 0     
                        iter_pres(row, cont)

                except Exception as e:
                    print('Error al iterar los elementos', str(e))
                
                try:
                    dataframe = create_df_pres(
                    data1, data2, data3, data4, data5, data6, data7
                    )
                except Exception as e:
                    print('Error al capturar data', str(e))
                
                try:
                    XlsxConst(dataframe, fechaConsulta, name)
                    clear_list()
                except Exception as e:
                    print('Error al construir DF', str(e))


                print('Fin de proceso Presentacion Manuales - Ejecutado correctamente')
                break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


def control_cierre_tarjetas():
    retry_count = 0
    while retry_count < max_retries:
        try:
            print('Inicio de proceso Control Cierre Tarjetas')
            query = query_cierre_tarj
            name = 'Cierre Tarjetas'

            results = consulta_query_cierre_tarjeta(query)

            try:
                print('Itera sobre el resultado')
                for row in results:
                    cont = 0
                    fechaCierre = row[12]
                    tipo = row[7]

                    if fechaCierre is None and tipo == 2:
                        iter_tarj_cierre(row, cont)
                    else:
                        pass

            except Exception as e:
                print('Error al iterar los elementos', str(e))
            

            if not data1:
                print('No hay movimientos para el periodo')
                send_mail_clear(fechaConsulta, name)
                break
            else:
                try:
                    dataframe = create_df_tarj_cierre(
                    data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14
                    )
                except Exception as e:
                    print('Error al capturar data', str(e))

                try:        
                    XlsxConstCierre(dataframe, fechaConsulta, name)
                    clear_list()
                except Exception as e:
                    print('Error al construir DF', str(e))

                print('Fin de proceso Control Cierre Tarjetas - Ejecutado correctamente')
                break

        except pyodbc.Error as e:
            if '1205' in str(e):
                retry_count += 1
                time.sleep(5)
            elif '1204' in str(e):
                retry_count += 1
                time.sleep(5)
            else:
                print('Error:', e)
                break


#-----------------------------------------------------------------------#


def control_promo_oca():
    query = query_promo
    name = 'Promo Oca'

    promo = '24'

    results = consulta_query_promo(query, promo)

    for row in results:
        cont = 0

        iter_promo(row, cont)

    dataframe = create_df_promo(
        data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13
        )
    
    XlsxConst(dataframe, fechaConsulta, name)
    clear_list()

    print('Fin de proceso')


#-----------------------------------------------------------------------#


#-----------------------------------------------------------------------#


def control_promo_itau():
    query = query_promo
    name = 'Promo Itau'

    promo = '83'

    results = consulta_query_promo(query, promo)

    for row in results:
        cont = 0

        iter_tarj(row, cont)

    dataframe = create_df_promo(
        data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, data20
        )
    
    XlsxConst(dataframe, fechaConsulta, name)
    clear_list()

    print('Fin de proceso')




#-------------------------------------------------------------------------------------#
