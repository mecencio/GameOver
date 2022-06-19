from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from products.models import Products
from GameOver.forms import userRegistrationForm, userLoginForm

# Create your views here.
def index(request):
    available_products = Products.objects.filter(inStock = True)
    context = {'available_products':available_products}
    return render(request, 'index.html', context=context)

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                context = {'error':'No hay ningún usuario con esas credenciales'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html',context=context)

        else:
            errors = form.errors
            form = userLoginForm()
            context = {'errors': errors, 'form':form}
            return render(request, 'auth/login.html', context=context)
    else:
        form = userLoginForm()
        context = {'form': form}
        return render(request, 'auth/login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/')

        else:
            errors = form.errors.as_dict() #Devuelve solo la descripción del error para cada error
            form = userRegistrationForm()
            context = {'errors': errors, 'form':form}
            return render(request, 'auth/register.html', context=context)

    else:
        form = userRegistrationForm()
        context = {'form':form}
        return render(request, 'auth/register.html', context=context)