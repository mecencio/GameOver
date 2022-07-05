from django import forms
from products.models import Category, Products
from about.models import cancelRequest, messagesContactUs

class addCategoryForm(forms.Form):
    name = forms.CharField(label='Nombre de la categoría', widget=forms.TextInput(attrs={'placeholder':'Nombre de la categoría','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))

class selectCategoryForm(forms.Form):
    category = forms.ModelChoiceField(queryset=None, label='Categoría', widget=forms.Select(attrs={'name':'Categoría', 'placeholder':'Categoría','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()

class addProductForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    price = forms.FloatField(label='Precio', widget=forms.TextInput(attrs={'name':'Precio', 'placeholder':'Precio','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    description = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'placeholder':'Descripción','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    brand = forms.CharField(label='Marca', widget=forms.TextInput(attrs={'placeholder':'Marca','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    model = forms.CharField(label='Modelo', widget=forms.TextInput(attrs={'placeholder':'Modelo','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    quantity = forms.IntegerField(label='Cantidad', widget=forms.TextInput(attrs={'name':'Cantidad', 'placeholder':'Cantidad','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    inStock = forms.BooleanField()
    image = forms.ImageField(label='Imagen del producto 1', widget=forms.FileInput(attrs={'name':'inputImage','id':'inputImage', 'class':'hidden'}))
    image2 = forms.ImageField(label='Imagen del producto 2', widget=forms.FileInput(attrs={'name':'inputImage2','id':'inputImage2', 'class':'hidden'}))
    image3 = forms.ImageField(label='Imagen del producto 3', widget=forms.FileInput(attrs={'name':'inputImage3','id':'inputImage3', 'class':'hidden'}))
    image4 = forms.ImageField(label='Imagen del producto 4', widget=forms.FileInput(attrs={'name':'inputImage4','id':'inputImage4', 'class':'hidden'}))
    image5 = forms.ImageField(label='Imagen del producto 5', widget=forms.FileInput(attrs={'name':'inputImage5','id':'inputImage5', 'class':'hidden'}))

    class Meta:
        model = Products
        fields = ['category', 'name', 'price', 'description', 'brand', 'model', 'quantity', 'inStock', 'image', 'image2', 'image3', 'image4', 'image5']
        help_texts = {k:'' for k in fields}

    def __init__(self, *args, **kwargs):
        super(addProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['inStock'].required = False
        self.fields['image'].required = False
        self.fields['image2'].required = False
        self.fields['image3'].required = False
        self.fields['image4'].required = False
        self.fields['image5'].required = False


class editCancelRequest(forms.ModelForm):
    STATUS_CHOICES = [
        ('Pedido ingresado', 'Pedido ingresado'),
        ('En gestión', 'En gestión'),
        ('Cancelación realizada', 'Cancelación realizada'),
        ('Cancelación rechazada', 'Cancelación rechazada'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Estado', widget=forms.Select(attrs={'placeholder':'Estado','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    response = forms.CharField(label='Respuesta', widget=forms.Textarea(attrs={'placeholder':'Indica el detalle de lo realizado sobre el pedido','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))

    class Meta:
        model = cancelRequest
        fields = ['status', 'response']
        help_texts = {k:'' for k in fields}

class editMessages(forms.ModelForm):
    STATUS_CHOICES = [
        ('Sin ver', 'Sin ver'),
        ('Visto', 'Visto'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Estado', widget=forms.Select(attrs={'placeholder':'Estado','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))
    response = forms.CharField(label='Respuesta', widget=forms.Textarea(attrs={'placeholder':'Indica el detalle sobre lo realizado','class':'w-full mt-2 py-3 px-6 bg-gray-200 rounded-xl'}))

    class Meta:
        model = messagesContactUs
        fields = ['status', 'response']
        help_texts = {k:'' for k in fields}