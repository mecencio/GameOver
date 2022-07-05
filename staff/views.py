from django.shortcuts import render, redirect
from staff.forms import addCategoryForm, selectCategoryForm, addProductForm, editCancelRequest, editMessages
from products.models import Category, Products
from about.models import cancelRequest, messagesContactUs
from orders.models import Order

# Create your views here.
def panel_view(request):
    if request.user.is_staff:
        return render(request, 'staff/panel.html')
    else:
        return redirect('/')

    #   ================
    #   CATEGORY OPTIONS
    #   ================

def add_category(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = addCategoryForm(request.POST)
            if form.is_valid():
                category = Category.objects.create(
                    name = form.cleaned_data['name']
                )
                category.save()
                form = addCategoryForm()
                context = {'message' : 'La categoría fue creada exitosamente', 'form': form}
                return render(request, 'staff/add-category.html', context=context)
            else:
                errors = form.errors.items()
                form = addCategoryForm()
                context = {'errors':errors, 'form':form}
                return render(request, 'staff/add-category.html', context=context)
        else:
            form = addCategoryForm()
            context = {'form':form}
            return render(request, 'staff/add-category.html', context=context)
    else:
        return redirect('/')

def modify_category_menu(request):
    if request.user.is_staff:
        categories = Category.objects.all()
        return render(request, 'staff/modify-category-menu.html', {'categories':categories})
    else:
        return redirect('/')

def modify_category(request, category_id):
    if request.user.is_staff:

        try:
            category = Category.objects.get(id=category_id)
        except:
            category = {}
        if category:
            if request.method == 'POST':
                form = addCategoryForm(request.POST)
                if form.is_valid():
                    category.name = form.cleaned_data['name']
                    category.save()
                    form = addCategoryForm(initial={
                        'name': category.name,
                    })
                    context = {'message' : 'La categoría fue modificada exitosamente', 'form': form, 'category':category}
                    return render(request, 'staff/modify-category.html', context=context)
                else:
                    errors = form.errors.items()
                    form = addCategoryForm(initial={
                        'name': category.name,
                    })
                    context = {'errors':errors, 'form':form, 'category':category}
                    return render(request, 'staff/modify-category.html', context=context)
            else:
                form = addCategoryForm(initial={
                        'name': category.name,
                    })
                context = {'form':form, 'category':category}
                return render(request, 'staff/modify-category.html', context=context)
        else:
            errors = 'La categoría no existe o es incorrecta'
            context = {'errors':errors}
            return render(request, 'staff/modify-category-menu.html', context=context)
    else:
        return redirect('/')

def delete_category(request, category_id, status):
    if request.user.is_staff:
        try:
            category = Category.objects.get(id=category_id)
        except:
            category = {}
        if category:
            if status == 'advertising':
                form = addCategoryForm(initial={
                    'name': category.name,
                })
                context = {
                    'advert' : 'Tenga en cuenta que este cambio es permanente y no podrá ser revertido. Si elimina esta categoría también estará eliminando todos los productos relacionados.', 
                    'category': category,
                    'form':form,
                    }
                return render(request, 'staff/modify-category.html', context=context)
            elif status == 'delete':
                    category.delete()
                    return redirect('/admin/modify-category/')
            else:
                return redirect('/admin/modify-category/')
        else:
            errors = 'La categoría no existe o es incorrecta'
            context = {'errors':errors}
            return render(request, 'staff/modify-category-menu.html', context=context)
    else:
        return redirect('/')

    #   ================
    #   PRODUCTS OPTIONS
    #   ================

def add_product(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = addProductForm(request.POST, request.FILES)
            try:
                category = Category.objects.get(id = request.POST['category'])
            except:
                category = {}
            if category:
                if form.is_valid():
                    product = Products.objects.create(
                        category = category,
                        name = form.cleaned_data['name'],
                        price = form.cleaned_data['price'],
                        description = form.cleaned_data['description'],
                        brand = form.cleaned_data['brand'],
                        model = form.cleaned_data['model'],
                        quantity = form.cleaned_data['quantity'],
                        inStock = form.cleaned_data['inStock'],
                        image = form.cleaned_data['image'],
                        image2 = form.cleaned_data['image2'],
                        image3 = form.cleaned_data['image3'],
                        image4 = form.cleaned_data['image4'],
                        image5 = form.cleaned_data['image5'],
                    )
                    product.save()
                    categoryform = selectCategoryForm()
                    form = addProductForm()
                    context = {'message' : 'El producto fue creado exitosamente', 'categoryform':categoryform, 'form': form}
                    return render(request, 'staff/add-product.html', context=context)
                else:
                    errors = form.errors.items()
                    categoryform = selectCategoryForm()
                    form = addProductForm(initial={
                        'quantity': 0,
                        'inStock': False,
                    })
                    context = {'errors':errors, 'categoryform':categoryform, 'form':form}
                    return render(request, 'staff/add-product.html', context=context)
            else:
                error = 'La categoría no existe o es incorrecta'
                categoryform = selectCategoryForm()
                form = addProductForm(initial={
                    'quantity': 0,
                    'inStock': False,
                })
                context = {'error':error, 'categoryform':categoryform, 'form':form}
                return render(request, 'staff/add-product.html', context=context)
        else:
            categoryform = selectCategoryForm()
            form = addProductForm(initial={
                'quantity': 0,
                'inStock': False,
            })
            context = {'categoryform':categoryform, 'form':form}
            return render(request, 'staff/add-product.html', context=context)
    else:
        return redirect('/')

def modify_product_menu(request):
    if request.user.is_staff:
        products = Products.objects.all()
        return render(request, 'staff/modify-product-menu.html', {'products':products})
    else:
        return redirect('/')

def modify_product(request, product_id):
    if request.user.is_staff:
        try:
            product = Products.objects.get(id = product_id)
        except:
            product ={}
        if product:
            if request.method == 'POST':
                form = addProductForm(request.POST, request.FILES)
                try:
                    category = Category.objects.get(id = request.POST['category'])
                except:
                    category = {}
                if category:
                    if form.is_valid():
                        product.category = category
                        product.name = form.cleaned_data['name']
                        product.price = form.cleaned_data['price']
                        product.description = form.cleaned_data['description']
                        product.brand = form.cleaned_data['brand']
                        product.model = form.cleaned_data['model']
                        product.quantity = form.cleaned_data['quantity']
                        product.inStock = form.cleaned_data['inStock']
                        if form.cleaned_data['image']:
                            product.image = form.cleaned_data['image']
                        if form.cleaned_data['image2']:
                            product.image2 = form.cleaned_data['image2']
                        if form.cleaned_data['image3']:
                            product.image3 = form.cleaned_data['image3']
                        if form.cleaned_data['image4']:
                            product.image4 = form.cleaned_data['image4']
                        if form.cleaned_data['image5']:
                            product.image5 = form.cleaned_data['image5']
                        product.save()
                        categoryform = selectCategoryForm(initial={
                            'name': product.category,
                        })
                        form = addProductForm(initial={
                            'name' : product.name,
                            'price' : product.price,
                            'description' : product.description,
                            'brand' : product.brand,
                            'model' : product.model,
                            'quantity' : product.quantity,
                            'inStock' : product.inStock,
                            'image' : product.image,
                            'image2' : product.image2,
                            'image3' : product.image3,
                            'image4' : product.image4,
                            'image5' : product.image5,
                        })
                        context = {'message' : 'El producto fue modificado exitosamente', 'categoryform':categoryform, 'form': form, 'product':product}
                        return render(request, 'staff/modify-product.html', context=context)
                    else:
                        errors = form.errors.items()
                        categoryform = selectCategoryForm(initial={
                            'name': product.category,
                        })
                        form = addProductForm(initial={
                            'name' : product.name,
                            'price' : product.price,
                            'description' : product.description,
                            'brand' : product.brand,
                            'model' : product.model,
                            'quantity' : product.quantity,
                            'inStock' : product.inStock,
                            'image' : product.image,
                            'image2' : product.image2,
                            'image3' : product.image3,
                            'image4' : product.image4,
                            'image5' : product.image5,
                        })
                        context = {'errors':errors, 'categoryform':categoryform, 'form':form, 'product':product}
                        return render(request, 'staff/modify-product.html', context=context)
                else:
                    error = 'La categoría no existe o es incorrecta'
                    categoryform = selectCategoryForm(initial={
                            'name': product.category,
                        })
                    form = addProductForm(initial={
                        'name' : product.name,
                        'price' : product.price,
                        'description' : product.description,
                        'brand' : product.brand,
                        'model' : product.model,
                        'quantity' : product.quantity,
                        'inStock' : product.inStock,
                        'image' : product.image,
                        'image2' : product.image2,
                        'image3' : product.image3,
                        'image4' : product.image4,
                        'image5' : product.image5,
                    })
                    context = {'error':error, 'categoryform':categoryform, 'form':form, 'product':product}
                    return render(request, 'staff/modify-product.html', context=context)
            else:
                categoryform = selectCategoryForm(initial={
                            'name': product.category,
                        })
                form = addProductForm(initial={
                    'name' : product.name,
                    'price' : product.price,
                    'description' : product.description,
                    'brand' : product.brand,
                    'model' : product.model,
                    'quantity' : product.quantity,
                    'inStock' : product.inStock,
                    'image' : product.image,
                    'image2' : product.image2,
                    'image3' : product.image3,
                    'image4' : product.image4,
                    'image5' : product.image5,
                })
                context = {'categoryform':categoryform, 'form':form, 'product':product}
                return render(request, 'staff/modify-product.html', context=context)
        else:
            products = Products.objects.all()
            errors = 'El producto no existe o es incorrecto'
            context = {'errors':errors, 'products':products}
            return render(request, 'staff/modify-product-menu.html', context=context)
    else:
        return redirect('/')


def delete_product(request, product_id, status):
    if request.user.is_staff:
        try:
            product = Products.objects.get(id = product_id)
        except:
            product ={}
        if product:
            if status == 'advertising':
                categoryform = selectCategoryForm(initial={
                    'name': product.category,
                })
                form = addProductForm(initial={
                    'name' : product.name,
                    'price' : product.price,
                    'description' : product.description,
                    'brand' : product.brand,
                    'model' : product.model,
                    'quantity' : product.quantity,
                    'inStock' : product.inStock,
                    'image' : product.image,
                    'image2' : product.image2,
                    'image3' : product.image3,
                    'image4' : product.image4,
                    'image5' : product.image5,
                })
                context = {
                    'advert' : 'Tenga en cuenta que este cambio es permanente y no podrá ser revertido.', 
                    'product': product,
                    'form': form,
                    'categoryform': categoryform
                    }
                return render(request, 'staff/modify-product.html', context=context)
            elif status == 'delete':
                    product.delete()
                    return redirect('/admin/modify-product/')
            else:
                return redirect('/admin/modify-product/')
        else:
            product = Products.objects.all()
            errors = 'El producto no existe o es incorrecto'
            context = {'errors':errors, 'products':product}
            return render(request, 'staff/modify-product-menu.html', context=context)
    else:
        return redirect('/')

    #   =======================
    #   VIEW REQUEST TO CANCEL
    #   =======================

def view_request_to_cancel(request):
    if request.user.is_staff:
        CancelRequest = cancelRequest.objects.all()
        return render(request, 'staff/request-cancel.html', {'CancelRequest':CancelRequest})
    else:
        return redirect('/')

def edit_request_to_cancel(request, request_id):
    if request.user.is_staff:
        try:
            CancelRequest = cancelRequest.objects.get(id = request_id)
        except:
            CancelRequest =  {}
        if CancelRequest:
            if request.method == 'POST':
                form = editCancelRequest(request.POST)
                if form.is_valid():
                    CancelRequest.status = form.cleaned_data['status']
                    CancelRequest.response = form.cleaned_data['response']
                    CancelRequest.employee = request.user.get_full_name()
                    CancelRequest.save()
                    form = editCancelRequest(initial={
                        'status': CancelRequest.status,
                        'response': CancelRequest.response,
                    })
                    return render(request, 'staff/edit-request-cancel.html', {'CancelRequest':CancelRequest, 'form' : form, 'success': 'El pedido fue actualizado con éxito'})
                else:
                    errors = form.errors.items()
                    form = editCancelRequest(initial={
                        'status': CancelRequest.status,
                        'response': CancelRequest.response,
                    })
                    context = {'errors':errors, 'form':form, 'CancelRequest':CancelRequest}
                    return render(request, 'staff/edit-request-cancel.html', context=context)
            else:
                form = editCancelRequest(initial={
                    'status': CancelRequest.status,
                    'response': CancelRequest.response,
                })
                return render(request, 'staff/edit-request-cancel.html', {'CancelRequest':CancelRequest, 'form' : form})
        else:
            CancelRequest = cancelRequest.objects.all()
            return redirect('/admin/request-to-cancel', {'CancelRequest':CancelRequest})
    else:
        return redirect('/')

    #   =================
    #    VIEW CONTACT US
    #   =================

def view_contact_us(request):
    if request.user.is_staff:
        messages = messagesContactUs.objects.all()
        return render(request, 'staff/messages.html', {'messages':messages})
    else:
        return redirect('/')

def edit_contact_us(request, message_id):
    if request.user.is_staff:
        try:
            message = messagesContactUs.objects.get(id = message_id)
        except:
            message =  {}
        if message:
            if request.method == 'POST':
                form = editMessages(request.POST)
                if form.is_valid():
                    message.status = form.cleaned_data['status']
                    message.response = form.cleaned_data['response']
                    message.employee = request.user.get_full_name()
                    message.save()
                    form = editMessages(initial={
                        'status': message.status,
                        'response': message.response,
                    })
                    return render(request, 'staff/edit-messages.html', {'message':message, 'form' : form, 'success': 'El pedido fue actualizado con éxito'})
                else:
                    errors = form.errors.items()
                    form = editMessages(initial={
                        'status': message.status,
                        'response': message.response,
                    })
                    context = {'errors':errors, 'form':form, 'message':message}
                    return render(request, 'staff/edit-messages.html', context=context)
            else:
                form = editMessages(initial={
                    'status': message.status,
                    'response': message.response,
                })
                return render(request, 'staff/edit-messages.html', {'message':message, 'form' : form})
        else:
            messages = messagesContactUs.objects.all()
            return redirect('/admin/messages', {'messages':messages})
    else:
        return redirect('/')

    #   ===============
    #     VIEW ORDERS
    #   ===============

def view_orders(request):
    if request.user.is_staff:
        orders = Order.objects.all()
        return render(request, 'staff/orders.html', {'orders':orders})
    else:
        return redirect('/')