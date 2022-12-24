from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .forms import escuelaForm, profesorForm, alumnoForm
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from MiApp.views import index, nuevo_taller, nuevo_profesor, nuevo_alumno, buscar_profesor, buscar_escuela,mostrar_profesor

# from ejemplo_dos.views import (index, PostDetalle, PostListar, 
#                                PostCrear, PostBorrar, PostActualizar,
#                                UserSignUp, UserLogin, UserLogout,
#                                MensajeDetalle, MensajeListar, MensajeCrear, MensajeBorrar,
#                                UserActualizar, AvatarActualizar)


urlpatterns = [
    path('', index),
    path('nuevo_taller/', nuevo_taller),
    path('nuevo_profesor/', nuevo_profesor),
    path('nuevo_alumno/', nuevo_alumno),
    path('buscar_escuela/', buscar_escuela),
    path('buscar_profesor/', buscar_profesor),
    path('escuelaForm/', escuelaForm),
    path('profesorForm/', profesorForm),
    path('alumnoForm/', alumnoForm),
    path('ver_profesor/', mostrar_profesor),  
    # path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    # path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    # path('ejemplo-dos/listar/', PostListar.as_view(), name="ejemplo-dos-listar"),
    # path('ejemplo-dos/crear/', staff_member_required(PostCrear.as_view()), name="ejemplo-dos-crear"),
    # path('ejemplo-dos/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="ejemplo-dos-borrar"),
    # path('ejemplo-dos/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="ejemplo-dos-actualizar"),
    # path('ejemplo-dos/signup/', UserSignUp.as_view(), name ="ejemplo-dos-signup"),
    # path('ejemplo-dos/login/', UserLogin.as_view(), name= "ejemplo-dos-login"),
    # path('ejemplo-dos/logout/', UserLogout.as_view(), name="ejemplo-dos-logout"),
    # path('ejemplo-dos/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="ejemplo-dos-mensajes-detalle"),
    # path('ejemplo-dos/mensajes/listar/', MensajeListar.as_view(), name="ejemplo-dos-mensajes-listar"),
    # path('ejemplo-dos/mensajes/crear/', MensajeCrear.as_view(), name="ejemplo-dos-mensajes-crear"),
    # path('ejemplo-dos/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="ejemplo-dos-mensajes-borrar"),
    # path('ejemplo-dos/about', TemplateView.as_view(template_name='ejemplo_dos/about.html'), name="ejemplo-dos-about"),
    # path('ejemplo-dos/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="ejemplo-dos-users-actualizar"),
    # path('ejemplo-dos/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="ejemplo-dos-avatars-actualizar"),
    
    
    ]   


