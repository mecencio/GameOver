from django import forms
from django.contrib.auth.models import User


class userOrderForm(forms.ModelForm):

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

    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'name':'first_name', 'placeholder':'Nombre','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'name':'last_name', 'placeholder':'Apellido','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'email', 'placeholder':'Ingresa tu email', 'class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    street = forms.CharField(label='Calle', widget=forms.TextInput(attrs={'name':'street', 'placeholder':'Calle','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    number = forms.IntegerField(label='Numero', widget=forms.TextInput(attrs={'name':'number', 'placeholder':'Numero','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    flat = forms.CharField(label='Piso', widget=forms.TextInput(attrs={'name':'flat', 'placeholder':'Piso','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    apartment = forms.CharField(label='Dpto', widget=forms.TextInput(attrs={'name':'apartment', 'placeholder':'Dpto','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    city = forms.CharField(label='Ciudad', widget=forms.TextInput(attrs={'name':'city', 'placeholder':'Ciudad','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    province = forms.CharField(label='Provincia', widget=forms.Select(choices=PROVINCE_CHOICES, attrs={'name':'province', 'placeholder':'Provincia','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    additionalInfo = forms.CharField(label='additionalInfo', widget=forms.TextInput(attrs={'name':'additionalInfo', 'placeholder':'Descripción de la fachada o indicaciones de referencia para ubicarla','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    code = forms.CharField(label='Cod Postal', widget=forms.TextInput(attrs={'name':'code', 'placeholder':'CP','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    phone = forms.CharField(label='Telefono', widget=forms.TextInput(attrs={'name':'phone', 'placeholder':'Telefono','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'street',
            'number',
            'flat',
            'apartment',
            'city',
            'province',
            'additionalInfo',
            'code',
            'phone',
        ]
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
        super(userOrderForm, self).__init__(*args, **kwargs)
        self.fields['flat'].required = False
        self.fields['apartment'].required = False
        self.fields['additionalInfo'].required = False