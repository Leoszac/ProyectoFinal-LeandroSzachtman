"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from MiApp.views import (index, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout,
                               MensajeDetalle, MensajeListar, MensajeCrear, MensajeBorrar,
                               UserActualizar, AvatarActualizar)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminsuccess_updated_message/',TemplateView.as_view(template_name="success_updated_message.html")),
    path('', index, name="index"),
    path('<int:pk>/detalle/', PostDetalle.as_view(), name="detalle"),
    path('listar/', PostListar.as_view(), name="listar"),
    path('crear/', staff_member_required(PostCrear.as_view()), name="crear"),
    path('<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="borrar"),
    path('<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="actualizar"),
    path('signup/', UserSignUp.as_view(), name ="signup"),
    path('login/', UserLogin.as_view(), name= "login"),
    path('logout/', UserLogout.as_view(), name="logout"),
    path('mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="mensajes-detalle"),
    path('mensajes/listar/', MensajeListar.as_view(), name="mensajes-listar"),
    path('mensajes/crear/', MensajeCrear.as_view(), name="mensajes-crear"),
    path('mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="mensajes-borrar"),
    path('about', TemplateView.as_view(template_name='about.html'), name="about"),
    path('users/<int:pk>/actualizar/', UserActualizar.as_view(), name="users-actualizar"),
    path('avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="avatars-actualizar"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)