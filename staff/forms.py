from django import forms
from products.models import Products

class addCategoryForm(forms.Form):
    name = forms.CharField(label='Nombre de la categoría', widget=forms.TextInput(attrs={'placeholder':'Nombre de la categoría','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
