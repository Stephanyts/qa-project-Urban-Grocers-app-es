import requests

import configuration

import data


# Realiza una solicitud GET para traer el authToken a la creación de cuenta de usuario.
def get_user_token(authToken):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        headers=authToken.headers) # inserta los encabezados

#Solicitud para crear un nuevo usuario o usuaria
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

#Solicitud para crear un kit personal para este usuario o usuaria
def post_new_kit(Autorization):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         headers=Autorization.headers)
    response = post_create_kit()

#Pasar el kit a formato json
def post_new_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers=data.headers)
    response = post_create_kit()
    print(response.json())
