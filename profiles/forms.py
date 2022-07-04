from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class userUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'placeholder':'Apellido','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Ingresa tu email', 'class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    image = forms.ImageField(label='Foto de Perfil', widget=forms.FileInput(attrs={'name':'inputImage','id':'inputImage', 'class':'hidden'}))
    description = forms.CharField(label='Descripcion', widget=forms.Textarea(attrs={'placeholder':'Escribí algo que quieras contarnos acerca de vos','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl', 'cols':5, 'rows':5}))
    phone = forms.CharField(label='Telefono', widget=forms.TextInput(attrs={'placeholder':'Telefono','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'image', 'description', 'phone']
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
        super(userUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['description'].required = False
        self.fields['phone'].required = False

class passwordUpdateForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'name':'inputPassword', 'placeholder':'Ingresa tu clave', 'class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput(attrs={'name':'inputPassword', 'placeholder':'Confirmá tu clave', 'class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    
    class Meta:
        model = User
        fields = ['password1', 'password2']
        help_texts = {k:'' for k in fields}


class addressForm(forms.ModelForm):
    PROVINCE_CHOICES = [
        ('Buenos Aires', 'Buenos Aires'),
        ('Ciudad Autónoma de Buenos Aires', 'Ciudad Autónoma de Buenos Aires'),
        ('Catamarca', 'Catamarca'),
        ('Chaco', 'Chaco'),
        ('Chubut', 'Chubut'),
        ('Córdoba', 'Córdoba'),
        ('Corrientes', 'Corrientes'),
        ('Entre Ríos', 'Entre Ríos'),
        ('Formosa', 'Formosa'),
        ('Jujuy', 'Jujuy'),
        ('La Pampa', 'La Pampa'),
        ('La Rioja', 'La Rioja'),
        ('Mendoza', 'Mendoza'),
        ('Misiones', 'Misiones'),
        ('Neuquén', 'Neuquén'),
        ('Río Negro', 'Río Negro'),
        ('Salta', 'Salta'),
        ('San Juan', 'San Juan'),
        ('San Luis', 'San Luis'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Santa Fe', 'Santa Fe'),
        ('Santiago del Estero', 'Santiago del Estero'),
        ('Tierra del Fuego', 'Tierra del Fuego'),
        ('Tucumán', 'Tucumán'),
    ]

    street = forms.CharField(label='Calle', widget=forms.TextInput(attrs={'name':'street', 'placeholder':'Calle','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    number = forms.IntegerField(label='Numero', widget=forms.TextInput(attrs={'name':'number', 'placeholder':'Numero','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    flat = forms.CharField(label='Piso', widget=forms.TextInput(attrs={'name':'flat', 'placeholder':'Piso','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    apartment = forms.CharField(label='Dpto', widget=forms.TextInput(attrs={'name':'apartment', 'placeholder':'Dpto','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    city = forms.CharField(label='Ciudad', widget=forms.TextInput(attrs={'name':'city', 'placeholder':'Ciudad','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    province = forms.CharField(label='Provincia', widget=forms.Select(choices=PROVINCE_CHOICES, attrs={'name':'province', 'placeholder':'Provincia','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    additionalInfo = forms.CharField(label='additionalInfo', widget=forms.TextInput(attrs={'name':'additionalInfo', 'placeholder':'Descripción de la fachada o indicaciones de referencia para ubicarla','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    code = forms.CharField(label='Cod Postal', widget=forms.TextInput(attrs={'name':'code', 'placeholder':'CP','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))

    class Meta:
        model = User
        fields = [
            'street',
            'number',
            'flat',
            'apartment',
            'city',
            'province',
            'additionalInfo',
            'code',
        ]
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
        super(addressForm, self).__init__(*args, **kwargs)
        self.fields['flat'].required = False
        self.fields['apartment'].required = False
        self.fields['additionalInfo'].required = False