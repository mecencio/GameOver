from django import forms
from about.models import cancelRequest, messagesContactUs


class cancelRequestForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder':'Nombre y apellido','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Ingresa tu email', 'class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    phone = forms.CharField(label='Telefono', widget=forms.TextInput(attrs={'placeholder':'Telefono','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    order = forms.CharField(label='Orden', widget=forms.TextInput(attrs={'placeholder':'Nro. de orden','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    description = forms.CharField(label='Descripcion', widget=forms.Textarea(attrs={'placeholder':'Introduzca aquí un comentario','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl', 'cols':5, 'rows':5}))


    class Meta:
        model = cancelRequest
        fields = ['name', 'email', 'phone', 'order', 'description']
        help_texts = {k:'' for k in fields}

class contactUsForm(forms.ModelForm):
    subject = forms.CharField(label='Asunto', widget=forms.TextInput(attrs={'placeholder':'Asunto','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Ingresa tu email', 'class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'placeholder':'Escríbenos un mensaje','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl', 'cols':5, 'rows':5}))

    class Meta:
        model = messagesContactUs
        fields = ['subject', 'email', 'message']