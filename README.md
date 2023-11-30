# Django Rest Framework First Project

Conocemos mas a detalle las herramientas que ofrece DRF sobre Django
## Creacion de un entorno virtual

 - [Guia Windows](https://micro.recursospython.com/recursos/como-crear-un-entorno-virtual-venv.html)

    1. Abre el CMD y ubícate en la carpeta en donde quieres crear el entorno virtual
    2. Ejecuta ```python -m venv mi_entorno```
    3. Ejecuta ```mi_entorno\Scripts\activate```
    


PD:
    Por cierto, es una buena práctica usar venv o env como los nombres del entorno virtual.
    Puedes activar el entorno virtual también haciendo ```mi_entorno\Scripts\activate.bat```, es exactamente lo mismo.
## Instalacion de librerias
Instala todas las librerias dentro de `requirements.txt`

```python
pip install -r requirements.txt
```

## Corre el proyecto en local

```
cd django_example
python manage.py runserver
```