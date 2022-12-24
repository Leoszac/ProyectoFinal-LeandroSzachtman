from django.shortcuts import render
from django.http import HttpResponse
from .models import profesor, escuela, alumno
from .forms import escuelaForm, profesorForm, alumnoForm


def index(request):
   return render(request, 'index.html')

######### BUSQUEDAS ##########


def buscar_profesor(request):
   data = request.GET.get('nombre', '')

   error = ''

   if data:
      try:
         PROD = profesor.objects.get(nombre = data)
         return render(request, 'consulta_profesor.html', {'PROD':PROD, 'nombre':data})
      except Exception as exc:
         error = 'no hay resultados'
   return render(request, 'consulta_profesor.html', {'error':error})


def buscar_escuela(request):
   data = request.GET.get('taller', '')

   error = ''

   if data:
      try:
         escuela = escuela.objects.get(deporte = data)
         return render(request, 'consulta_deporte.html', {'escuela':escuela, 'nombre':data})
      except Exception as exc:
         error = 'no hay resultados'
   return render(request, 'consulta_taller.html', {'error':error})


######### INGRESOS  ##########
def nuevo_taller(request):
   if request.method == 'POST':
      
      formulario_ND = escuelaForm(request.POST)
   
      if formulario_ND.is_valid():
         
         formulario_ND_limpio = formulario_ND.cleaned_data
         
         nuevo_taller = escuela(taller=formulario_ND_limpio['taller'])
         
         nuevo_taller.save()
         
         return render(request, 'index.html')

   else:
      formulario_ND = escuelaForm()
      return render(request, 'nuevo_taller.html', {'formulario_ND': formulario_ND})

def nuevo_profesor(request):
   if request.method == 'POST':
      
      formulario_NP = profesorForm(request.POST)
      
      if formulario_NP.is_valid():
         
         formulario_NP_limpio = formulario_NP.cleaned_data
         
         nuevo_profesor = profesor(nombre=formulario_NP_limpio['nombre'], DNI=formulario_NP_limpio['DNI'], taller=formulario_NP_limpio['taller'])
         
         nuevo_profesor.save()
         
         return render(request, 'index.html')

   else:
      formulario_NP = profesorForm()
      
      return render(request, 'nuevo_profesor.html', {'formulario_NP': formulario_NP})

def nuevo_alumno(request):
   if request.method == 'POST':
      
      formulario_NA = alumnoForm(request.POST)
      
      if formulario_NA.is_valid():
         
         formulario_NA_limpio = formulario_NA.cleaned_data
         
         nuevo_alumno = alumno(taller=formulario_NA_limpio['taller'], nombre=formulario_NA_limpio['nombre'], DNI=formulario_NA_limpio['DNI'])
         
         nuevo_alumno.save()
         
         return render(request, 'index.html')

   else:
      formulario_NA = alumnoForm()
      
      return render(request, 'nuevo_alumno.html', {'formulario_NA': formulario_NA})

######### Mostrar  ##########

def mostrar_profesor(request):
  lista_profesores = profesor.objects.all()  
  lista_talleres= escuela.objects.all()

  return render(request, "ver_todo.html", {"lista_profesores": lista_profesores, "lista_talleres": lista_talleres})

######### Actualizar  ##########





# from django.shortcuts import render
# from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
# from ejemplo_dos.models import Post, Mensaje
# from django.urls import reverse_lazy
# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# from ejemplo_dos.forms import UsuarioForm
# from ejemplo_dos.models import Avatar
# from django.contrib.auth.admin import User


# def index(request):
#     posts = Post.objects.order_by("-id").all()
#     return render(request, "ejemplo_dos/index.html", {"posts": posts})

# class PostDetalle(DetailView):
#     model = Post

# class PostListar(ListView):
#     model = Post  

# class PostCrear(LoginRequiredMixin, CreateView):
#     model = Post
#     success_url = reverse_lazy("ejemplo-dos-listar")
#     fields = '__all__'

# class PostBorrar(LoginRequiredMixin, DeleteView):
#     model = Post
#     success_url = reverse_lazy("ejemplo-dos-listar")

# class PostActualizar(LoginRequiredMixin, UpdateView):
#     model = Post
#     success_url = reverse_lazy("ejemplo-dos-listar")
#     fields = "__all__"

# class UserSignUp(CreateView):
#     form_class = UsuarioForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('ejemplo-dos-listar')

# #http://localhost:8000/ejemplo-dos/login/?next=/ejemplo-dos/listar/
# class UserLogin(LoginView):
#     next_page = reverse_lazy('ejemplo-dos-listar')

# class UserLogout(LogoutView):
#     next_page = reverse_lazy('ejemplo-dos-listar')

# class MensajeDetalle(DetailView):
#     model = Mensaje

# class MensajeListar(LoginRequiredMixin, ListView):
#     model = Mensaje  

# class MensajeCrear(SuccessMessageMixin, CreateView):
#     model = Mensaje
#     success_url = reverse_lazy("ejemplo-dos-mensajes-crear")
#     fields = ['nombre', 'email', 'texto']
#     success_message = "Mensaje de contacto enviado!!"

# class MensajeBorrar(LoginRequiredMixin, DeleteView):
#     model = Mensaje
#     success_url = reverse_lazy("ejemplo-dos-mensajes-listar")

# class UserActualizar(UpdateView):
#     model = User
#     fields = ['first_name', 'last_name', 'email']
#     success_url = reverse_lazy('ejemplo-dos-listar')

# class AvatarActualizar(UpdateView):
#     model = Avatar
#     fields = ['imagen']
#     success_url = reverse_lazy('ejemplo-dos-listar')