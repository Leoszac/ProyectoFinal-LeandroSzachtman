# Proyecto Final - Leandro Szachtman
Proyecto final de CoderHouse
Blog en Django

Este es un proyecto de un blog creado con Django, un framework de Python para el desarrollo de aplicaciones web.

## Requisitos
Para poder utilizar este proyecto, es necesario tener instalado lo siguiente:

Python 3.6 o superior
Django 2.2 o superior
También se recomienda utilizar un gestor de paquetes como pip para facilitar la instalación de las dependencias.

## Instalación
1. Clona este repositorio en tu computadora
Crea un entorno virtual y activa el entorno 

2. Instala las dependencias necesarias ejecutando el siguiente comando:
pip install -r requirements.txt

3. Realiza las migraciones necesarias ejecutando los siguientes comandos:
python manage.py makemigrations
python manage.py migrate

4. Crea un superusuario para poder acceder al panel de administración ejecutando el siguiente comando:
python manage.py createsuperuser
Usuario creado: admin
Password: 1234admin1234

5. Arranca el servidor de desarrollo ejecutando el siguiente comando:
python manage.py runserver

Ahora puedes acceder al blog en tu navegador preferido escribiendo la dirección http://127.0.0.1:8000/. Para acceder al panel de administración del blog, ve a http://127.0.0.1:8000/admin/ y utiliza las credenciales del superusuario que creaste anteriormente.


## Características
Modelos: 4
ListView: Implementado --> /listar
DetailView: Implementado --> <int:pk>/detalle>
UpdateView: Implementado --> <int:pk>/actualizar/
DeleteView: Implementado --> <int:pk>/borrar
CreateView: Implementado --> /crear
Registro de nuevos users: Implementado --> /Signup
Profile Update: Implementado --> users/<int:pk>/actualizar
Login: Implementado --> /login
Logout: Implementado -->  /logout
Login Required: Implementado --> <int:pk>/actualizar/
About: Implementado --> /about

## VIDEO:
https://youtu.be/-o_rtYKFXUQ