# Urban.Grocers API Testing Project

## Descripción

Este proyecto se centra en la automatización de pruebas para la API de Urban.Grocers, una plataforma que permite la creación de kits de alimentos personalizados. Las pruebas se realizaron para asegurar la correcta funcionalidad de los endpoints relacionados con la creación y gestión de kits de alimentos.

## Objetivos del Proyecto

- Verificar la correcta creación de kits de alimentos.
- Asegurar la integridad de los datos enviados y recibidos.
- Validar las respuestas de la API para diferentes escenarios de prueba.

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python
- **Framework de Pruebas:** Pytest
- **Herramientas Adicionales:** Git, GitHub, Postman

## Endpoints Probados

- **POST /kits:** Creación de un nuevo kit de alimentos.
- **GET /kits/{id}:** Obtención de detalles de un kit específico.

## Estructura del Proyecto

- `Configuration.py`: Archivos de configuración y variables de entorno.
- `data.py`: Funciones y utilidades comunes para las pruebas.
- `sender_stand_request.py`: Pruebas para la creación de kits.
- `create_kit_name_kit_test.py`: Contiene todos los archivos de prueba.

## Pruebas automatizadas en archivo create_kit_name_test.py

- Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracteres
- - def test_create_kit_1_letter_in_name_get_success_response()
- Prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres
- - def test_create_kit_511_letters_in_name_get_success_response()
- Prueba 3. Error. El parámetro contiene un string vacío
- - def test_create_kit_empty_name_get_error_response()
- Prueba 4. Error. El parámetro name contiene 512 caracteres
- - def test_create_kit_512_letters_in_name_get_error_response()
- Prueba 5. El parámetro name contiene un string de caracteres especiales
- - def test_create_kit_special_caracaters_get_success_response()
- Prueba 6. El parámetro name contiene espacios
- - def test_create_kit_white_space_get_success_response()
- Prueba 7. El parámetro name contiene un string de dígitos
- - def test_create_kit_numbers_allowed_get_success_response()
- Prueba 8. Error. Falta el parametro name en la solicitud
- - def negative_assert_no_name_error_response()
- Prueba 9. Error. El tipo del parámetro name: número
- - def test_create_kit_number_type_get_error_response
  
## Cómo Ejecutar las Pruebas

1. Clonar el repositorio:
   ```bash
   git clone https://stephanyts/urban-grocers-api-testing.git

Navegar al directorio del proyecto:
cd urban-grocers-api-testing

Instalar las dependencias:
pip install -r requirements.txt

Ejecutar las pruebas:
pytest

Contribuciones
¡Las contribuciones son bienvenidas! Por favor, sigue los siguientes pasos para contribuir:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
Sube tus cambios (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
Contacto
Para cualquier duda o sugerencia, por favor contacta a stephanyts54@gmail.com

¡Gracias por tu interés en el proyecto Urban.Grocers API Testing!
