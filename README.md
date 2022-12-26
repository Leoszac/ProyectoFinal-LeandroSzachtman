# Proyecto Final - Leandro Szachtman
Proyecto final de CoderHouse</br>
Blog en Django</br>

Este es un proyecto de un blog creado con Django, un framework de Python para el desarrollo de aplicaciones web.</br>

## Requisitos
Para poder utilizar este proyecto, es necesario tener instalado lo siguiente:</br></br>

Python 3.6 o superior</br>
Django 2.2 o superior</br>
También se recomienda utilizar un gestor de paquetes como pip para facilitar la instalación de las dependencias.</br>

## Instalación
1. Clona este repositorio en tu computadora</br>
Crea un entorno virtual y activa el entorno </br>

2. Instala las dependencias necesarias ejecutando el siguiente comando:</br>
pip install -r requirements.txt</br>

3. Realiza las migraciones necesarias ejecutando los siguientes comandos:</br>
python manage.py makemigrations</br>
python manage.py migrate</br>

4. Crea un superusuario para poder acceder al panel de administración ejecutando el siguiente comando:</br>
python manage.py createsuperuser</br>
Usuario creado: admin</br>
Password: 1234admin1234</br>

5. Arranca el servidor de desarrollo ejecutando el siguiente comando:
python manage.py runserver

Ahora puedes acceder al blog en tu navegador preferido escribiendo la dirección http://127.0.0.1:8000/. Para acceder al panel de administración del blog, ve a http://127.0.0.1:8000/admin/ y utiliza las credenciales del superusuario que creaste anteriormente.


## Características
Modelos: 4
ListView: Implementado --> /listar </br>
DetailView: Implementado --> <int:pk>/detalle> </br>
UpdateView: Implementado --> <int:pk>/actualizar/</br>
DeleteView: Implementado --> <int:pk>/borrar</br>
CreateView: Implementado --> /crear</br>
Registro de nuevos users: Implementado --> /Signup</br>
Profile Update: Implementado --> users/<int:pk>/actualizar</br>
Login: Implementado --> /login</br>
Logout: Implementado -->  /logout</br>
Login Required: Implementado --> <int:pk>/actualizar/</br>
About: Implementado --> /about</br>

## VIDEO:
https://youtu.be/-o_rtYKFXUQ