import pandas as pd
from variables import output_folder, rute_path
from send_mail import *
#---------------------------------------------------------#

#---------------------------------------------------------#
def XlsxConst(dataframe, fechaConsulta, name):
    output_folder.mkdir(parents=True, exist_ok=True)
    excel_path = f'{output_folder}/{name} - {fechaConsulta}.xlsx'
    dataf = pd.DataFrame(dataframe)
    dataf.to_excel(excel_path, index=False)    


    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(send_mail(excel_path, fechaConsulta, name))

    if result:
        print('Mensaje enviado')
    else:
        print('No enviado')


def XlsxConstCierre(dataframe, fechaConsulta, name):
    output_folder.mkdir(parents=True, exist_ok=True)
    excel_path = f'{output_folder}/{name} - {fechaConsulta}.xlsx'
    dataf = pd.DataFrame(dataframe)
    dataf.to_excel(excel_path, index=False)    


    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(send_mail_cierre(excel_path, fechaConsulta, name))

    if result:
        print('Mensaje enviado')
    else:
        print('No enviado')
