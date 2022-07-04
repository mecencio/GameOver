from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from profiles.models import userAddresses, userProfile
from profiles.forms import userUpdateForm, addressForm, passwordUpdateForm
from orders.models import Order
from about.models import cancelRequest


# Create your views here.

    #   =============
    #   PROFILE PAGE
    #   =============

@login_required
def my_profile_view(request):
    try:
        user = userProfile.objects.get(user=request.user)
    except:
        user = userProfile.objects.create(user=request.user)
    if request.method == 'POST':
        form = userUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            if form.cleaned_data['image']:
                user.image = form.cleaned_data['image']
            user.description = form.cleaned_data['description']
            user.phone = form.cleaned_data['phone']
            user.save()
            return redirect('/my-profile')
        else:
            errors = form.errors.items()
            form = userUpdateForm(initial={
                'first_name':request.user.first_name,
                'last_name':request.user.last_name,
                'email':request.user.email,
                'image':user.image,
                'description':user.description,
                'phone':user.phone,
            })
            context= {'errors':errors, 'form':form}
            return render(request, 'my-profile/my-profile.html', context=context)
    else:
        form = userUpdateForm(initial={
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'email':request.user.email,
            'image':user.image,
            'description':user.description,
            'phone':user.phone,
        })
        context= {'form':form}
        return render(request, 'my-profile/my-profile.html', context=context)

@login_required
def delete_image(request):
    request.user.profile.image.delete()
    return redirect('/my-profile')


    #   ===============
    #   PURCHASES PAGE
    #   ===============

@login_required
def my_purchases_view(request):
    orders = Order.objects.filter(user= request.user)
    context = {}
    context['orders'] = orders
    try:
        cancelOrder = cancelRequest.objects.filter(user=request.user)
        context['cancelOrder'] = cancelOrder
    except:
        pass
    return render(request, 'my-profile/my-purchases.html', context=context)


    #   =============
    #   ADDRESS PAGE
    #   =============

@login_required
def address_view(request):
    addresses = userAddresses.objects.filter(user= request.user)
    context = {'addresses':addresses}
    return render(request, 'my-profile/addresses.html', context=context)

@login_required
def add_address_view(request):
    if request.method == 'POST':
        form = addressForm(request.POST)
        if form.is_valid():
            userAddresses.objects.create(
                user=request.user, 
                street = form.cleaned_data['street'], 
                number = form.cleaned_data['number'], 
                flat = form.cleaned_data['flat'], 
                apartment = form.cleaned_data['apartment'], 
                city = form.cleaned_data['city'], 
                province = form.cleaned_data['province'], 
                additionalInfo = form.cleaned_data['additionalInfo'], 
                code = form.cleaned_data['code'], 
            )
            return redirect('/my-profile/addresses')
        else:
            errors = form.errors.items()
            form = addressForm()
            context= {'errors':errors, 'form':form}
            return render(request, 'my-profile/add-address.html', context=context)
    else:
        form = addressForm()
        context= {'form':form}
        return render(request, 'my-profile/add-address.html', context=context)

@login_required
def delete_address_view(request, address_id):
    userAddresses.objects.get(pk=address_id).delete()
    return redirect('/my-profile/addresses')

@login_required
def edit_address_view(request, address_id):
    address = userAddresses.objects.get(pk=address_id)
    if request.method == 'POST':
        form = addressForm(request.POST)
        if form.is_valid():
            address.street = form.cleaned_data['street']
            address.number = form.cleaned_data['number']
            address.flat = form.cleaned_data['flat']
            address.apartment = form.cleaned_data['apartment']
            address.city = form.cleaned_data['city']
            address.province = form.cleaned_data['province']
            address.additionalInfo = form.cleaned_data['additionalInfo']
            address.code = form.cleaned_data['code']
            address.save()
            return redirect('/my-profile/addresses')
        else:
            errors = form.errors.items()
            form = addressForm(initial={
                'street': address.street,
                'number': address.number,
                'flat': address.flat,
                'apartment': address.apartment,
                'city': address.city,
                'province': address.province,
                'additionalInfo': address.additionalInfo,
                'code': address.code,
            })
            context= {'errors':errors, 'form':form, 'address':address}
            return render(request, 'my-profile/edit-address.html', context=context)
    else:
        form = addressForm(initial={
            'street': address.street,
            'number': address.number,
            'flat': address.flat,
            'apartment': address.apartment,
            'city': address.city,
            'province': address.province,
            'additionalInfo': address.additionalInfo,
            'code': address.code,
        })
        context= {'form':form, 'address':address}
        return render(request, 'my-profile/edit-address.html', context=context)


    #   =============
    #   SECURITY PAGE
    #   =============

@login_required
def user_security_view(request):
    if request.method == 'POST':
        form = passwordUpdateForm(request.POST)
        if form.is_valid():
            if request.user.check_password(request.POST['oldpassword']):
                username = request.user
                password = form.cleaned_data['password1']
                username.set_password(password)
                username.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/my-profile')
            else:
                errors = [('password',['La contraseña actual es incorrecta'])]
                form = passwordUpdateForm()
                context= {'errors':errors, 'form':form}
                return render(request, 'my-profile/user-security.html', context=context)
        else:
            errors = list(form.errors.items())
            if not request.user.check_password(request.POST['oldpassword']):
                errors.append(('password',['La contraseña actual es incorrecta']))
            form = passwordUpdateForm()
            context= {'errors':errors, 'form':form}
            return render(request, 'my-profile/user-security.html', context=context)
    else:
        form = passwordUpdateForm()
        context= {'form':form}
        return render(request, 'my-profile/user-security.html', context=context)

def delete_account_view(request, status):
        if status == 'advertising':
            form = passwordUpdateForm()
            context = {'message' : 'Tenga en cuenta que este cambio es permanente y no podrá ser revertido', 'form':form}
            return render(request, 'my-profile/user-security.html', context=context)
        elif status == 'delete':
            if request.method == 'POST':
                if request.user.check_password(request.POST['password']):
                    request.user.delete()
                    return redirect('/')
                else:
                    message = 'Tenga en cuenta que este cambio es permanente y no podrá ser revertido'
                    password = 'La contraseña ingresada es incorrecta'
                    form = passwordUpdateForm()
                    context= {'message':message, 'password':password,'form':form}
                    return render(request, 'my-profile/user-security.html', context=context)
            else:
                return redirect('/my-profile/security/')
        else:
            errors = form.errors.items()
            form = passwordUpdateForm()
            context= {'errors':errors, 'form':form}
            return render(request, 'my-profile/user-security.html', context=context)