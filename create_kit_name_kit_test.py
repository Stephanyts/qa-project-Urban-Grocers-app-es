import sender_stand_request

import data

# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    kit_response = sender_stand_request.post_new_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert kit_response.json()["authToken"] != ""

    # Comprobar que el resultado de la solicitud se guarda en users_table_response
    kit_table_response = sender_stand_request.get_kit_table()

    # String que debe estar en el cuerpo de respuesta
    str_kit = kit_body["name"] + \
               ",,," + kit_response.json()["authToken"]

    # Comprueba si el kit existe y es único
    assert kit_table_response.text.count(str_kit) == 1

# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_symbol(name):
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    kit_body = get_kit_body(name)

    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

def negative_assert_no_name(kit_body):
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_kit(kit_body)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

# Prueba 1. kit creado con éxito. El parámetro name contiene 1 caracteres
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                "bcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda" 
                "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                "cdabcdabcdabcdabcdabcdabC")

#Prueba 3. Error. El parámetro contiene un string vacío
def test_create_kit_empty_name_get_error_response():
    #El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = get_kit_body("")
    #Comprueba la respuesta
    negative_assert_no_name(kit_body)

# Prueba 4. Error. El parámetro name contiene 512 caracteres
def test_create_kit_512_letters_in_name_get_error_response():
        negative_assert_symbol("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab" 
               "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
               "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
               "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdab"
               "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
               "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
               "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5. El parámetro name contiene un string de caracteres especiales
def test_create_kit_special_caracaters_get_success_response():
    positive_assert("\"№%@\",")

# Prueba 6. El parámetro name contiene espacios
def test_create_kit_white_space_get_success_response():
    positive_assert(" A Aaa ")

# Prueba 7. El parámetro name contiene un string de dígitos
def test_create_kit_numbers_allowed_get_success_response():
    positive_assert("123")

#prueba 8. Error. Falta el parámetro name en la solicitud
def negative_assert_no_name_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_name(kit_body)

# Prueba 9. Error. El tipo del parámetro name: número
def test_create_kit_number_type_get_error_response():
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = get_kit_body(123)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_kit(kit_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400
