import requests

import configuration

import data

#Solicitud para crear un nuevo usuario o usuaria
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

#Solicitud para crear un kit personal para este usuario o usuaria
def post_new_kit(kit_body,auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=auth_token)
