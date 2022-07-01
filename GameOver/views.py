from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from products.models import Products
from GameOver.models import userAddresses
from GameOver.forms import userRegistrationForm, userLoginForm, userUpdateForm

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
    if request.user.is_authenticated:
        return redirect('/my-profile')
    else:
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
                errors = form.errors.items()
                form = userRegistrationForm()
                context = {'errors': errors, 'form':form}
                return render(request, 'auth/register.html', context=context)

        else:
            form = userRegistrationForm()
            context = {'form':form}
            return render(request, 'auth/register.html', context=context)

def my_profile_view(request):
    if request.user.is_authenticated:
        orders = request.user.orders.all()[:5]
        return render(request, 'my-profile/my-profile.html', {'orders':orders})
    else:
        return redirect('/login')

def address_view(request):
    addresses = userAddresses.objects.filter(user= request.user)
    context = {'addresses':addresses}
    return render(request, 'my-profile/addresses.html', context=context)

def delete_address_view(request, address_id):
    userAddresses.objects.get(pk=address_id).delete()
    return redirect('/addresses')

def edit_address_view(request, address_id):
    address = userAddresses.objects.get(pk=address_id)
    if request.method == 'POST':
        address.street = request.POST.get('street')
        address.number = request.POST.get('number')
        address.flat = request.POST.get('flat')
        address.apartment = request.POST.get('apartment')
        address.city = request.POST.get('city')
        address.province = request.POST.get('province')
        address.additionalInfo = request.POST.get('additionalInfo')
        address.code = request.POST.get('code')
        address.save()
        return redirect('/addresses')
    else:
        context= {'address':address}
        return render(request, 'my-profile/edit-address.html', context=context)

def edit_information_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = userUpdateForm(request.POST)
            if form.is_valid():
                user = request.user
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.save()
                return redirect('/my-profile')

            else:
                errors = form.errors.items()
                form = userUpdateForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email})
                context = {'errors': errors, 'form':form}
                return render(request, 'my-profile/edit-information.html', context=context)

        else:
            form = userUpdateForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email})
            context = {'form':form}
            return render(request, 'my-profile/edit-information.html', context=context)

    else:
        return redirect('/login')