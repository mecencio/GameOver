from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'inputEmail', 'placeholder':'Ingresa tu email', 'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'name':'inputPassword', 'placeholder':'Ingresa tu clave', 'class':'form-control'}))
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput(attrs={'name':'inputPassword', 'placeholder':'Confirmá tu clave', 'class':'form-control'}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'name':'inputLastName', 'placeholder':'Apellido','class':'form-control'}))
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'name':'inputName', 'placeholder':'Nombre','class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'name':'inputUsername', 'placeholder':'Ingresa tu usuario', 'autocomplete':'username', 'class':'form-control'}),
        }
        help_texts = {k:'' for k in fields}

class userUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'inputEmail', 'placeholder':'Ingresa tu email', 'class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'name':'inputLastName', 'placeholder':'Apellido','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'name':'inputName', 'placeholder':'Nombre','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
        super(userUpdateForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = False

class userLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'name':'inputUsername', 'placeholder':'Ingresa tu usuario', 'required':'', 'autocomplete':'username', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name':'inputPassword', 'placeholder':'Ingresa tu clave', 'required':'', 'class':'form-control'}))

    class Meta:
        fields = ['username', 'password']