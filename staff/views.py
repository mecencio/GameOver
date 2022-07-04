from django.shortcuts import render, redirect
from staff.forms import addCategoryForm
from products.models import Category

# Create your views here.
def panel_view(request):
    if request.user.is_staff:
        return render(request, 'staff/panel.html')
    else:
        return redirect('/')

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