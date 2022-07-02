from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.models import userAddresses, userProfile
from profiles.forms import userUpdateForm, addressForm
from orders.models import Order


# Create your views here.
@login_required
def my_profile_view(request):
    # try:
    #     user = userProfile.objects.get(user=request.user)
    # except:
    #     user = userProfile.objects.create(user=request.user)
    user = request.user
    if request.method == 'POST':
        form = userUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form)
            user.first_name = form.cleaned_data['first_name'], 
            user.last_name = form.cleaned_data['last_name'], 
            user.email = form.cleaned_data['email'],
            if form.cleaned_data['image']:
                user.profile.image = form.cleaned_data['image'], 
            if form.cleaned_data['description']:
                user.profile.description = form.cleaned_data['description'], 
            if form.cleaned_data['phone']:
                user.profile.phone = form.cleaned_data['phone'],
            user.save()
            return redirect('/my-profile')
        else:
            errors = form.errors.items()
            form = userUpdateForm(initial={
                'first_name':request.user.first_name,
                'last_name':request.user.last_name,
                'email':request.user.email,
                'image':user.profile.image,
                'description':user.profile.description,
                'phone':user.profile.phone,
            })
            context= {'errors':errors, 'form':form}
            return render(request, 'my-profile/my-profile.html', context=context)
    else:
        form = userUpdateForm(initial={
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'email':request.user.email,
            'image':user.profile.image,
            'description':user.profile.description,
            'phone':user.profile.phone,
        })
        context= {'form':form}
        return render(request, 'my-profile/my-profile.html', context=context)

@login_required
def address_view(request):
    addresses = userAddresses.objects.filter(user= request.user)
    context = {'addresses':addresses}
    return render(request, 'my-profile/addresses.html', context=context)

@login_required
def my_purchases_view(request):
    orders = Order.objects.filter(user= request.user)
    context = {'orders':orders}
    return render(request, 'my-profile/my-purchases.html', context=context)

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

@login_required
def edit_information_view(request):
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