from django import forms

    
class escuelaForm(forms.Form):
    taller = forms.CharField(max_length = 100)
    
class profesorForm(forms.Form):
    taller = forms.CharField(max_length = 100)
    nombre = forms.CharField(max_length = 100)
    DNI = forms.IntegerField()


class alumnoForm(forms.Form):
    taller = forms.CharField(max_length = 100)
    nombre = forms.CharField(max_length = 100)
    DNI = forms.IntegerField()
    

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.admin import User

# class UsuarioForm(UserCreationForm):
#     username = forms.CharField(max_length=20)

#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']

