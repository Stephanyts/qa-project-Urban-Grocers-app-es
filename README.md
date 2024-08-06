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
