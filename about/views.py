from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from about.models import cancelRequest
from about.forms import cancelRequestForm, contactUsForm

# Create your views here.
def privacy_policy_view(request):
    return render(request, 'about/privacy-policy.html')

def contact_us_view(request):
    if request.method == 'POST':
        form = contactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            errors = form.errors.items()
            form = contactUsForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'about/contact-us.html', context=context)
    else:
        form = contactUsForm()
        context = {'form':form}
        return render(request, 'about/contact-us.html', context=context)

def about_us_view(request):
    return render(request, 'about/about-us.html')

def faq_view(request):
    return render(request, 'about/faq.html')

@login_required
def cancel_request_view(request):
    if request.method == 'POST':
        form = cancelRequestForm(request.POST)
        if form.is_valid():
            cancelOrder = cancelRequest.objects.create(
                user = request.user, 
                name = form.cleaned_data['name'], 
                email = form.cleaned_data['email'], 
                phone = form.cleaned_data['phone'], 
                order = form.cleaned_data['order'], 
                description = form.cleaned_data['description'], 
            )
            cancelOrder.save()
            return redirect('/my-profile/my-purchases/')
        else:
            errors = form.errors.items()
            form = cancelRequestForm(initial={
                'name':request.user.get_full_name(),
                'email':request.user.email,
                'phone':request.user.profile.phone,
            })
            context= {'errors':errors, 'form':form}
            return render(request, 'about/cancel-buy.html', context=context)
    else:
        form = cancelRequestForm(initial={
                'name':request.user.get_full_name(),
                'email':request.user.email,
                'phone':request.user.profile.phone,
        })
        context= {'form':form}
        return render(request, 'about/cancel-buy.html', context=context)

@login_required
def delete_cancel_request_view(request, request_id):
    cancelRequest.objects.get(pk=request_id).delete()
    return redirect('/my-profile/my-purchases/')