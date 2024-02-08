import sys
import os
import django
import asyncio

from variables import project_directory, adressee_cajas, adressee_cierre_tarj

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
#--------------------------------------------------------------#

sys.path.append(project_directory)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ReportPython.settings")
django.setup()

#--------------------------------------------------------------#

text_cierre_tarjetas = 'Cerraron todas las tarjetas correctamente'


async def send_mail(excel_path, date_process, name):
    await asyncio.sleep(2)
    try:
        subject = f"Documentos para controlar {name} - {date_process}"
        message = render_to_string('mail_cajas.html', {
            'nameFile': excel_path,
            'fecha': date_process,
        })
        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER,
                adressee_cajas)
        email.attach_file(excel_path)
        await email.send()
        return True
    
    except Exception as e:
        print(str(e))
        return False


async def send_mail_cierre(excel_path, date_process, name):
    await asyncio.sleep(2)
    try:
        subject = f"Documentos para controlar {name} - {date_process}"
        message = render_to_string('mail_cajas.html', {
            'nameFile': excel_path,
            'fecha': date_process,
        })
        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER,
                adressee_cierre_tarj)
        email.attach_file(excel_path)
        await email.send()
        return True
    
    except Exception as e:
        print(str(e))
        return False
    

def send_mail_clear(date_process, name):
    if name == 'Cierre Tarjetas':
        text = text_cierre_tarjetas
    else:
        text = f'No se encuntraron registros para {name}'

    try:
        subject = f"{text} - {date_process}"
        message = render_to_string('mail_clear_cajas.html', {
            'fecha': date_process,
            'name' : name,
            'text':f'{text} el {date_process}'
        })
        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER,
                adressee_cajas)
        email.send()
        return True
    
    except Exception as e:
        print(str(e))
        return False
