from django.shortcuts import render, redirect
from products.forms import ProductsForm
from products.models import Products

# Create your templates here.
def products(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ProductsForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    shoes = Products.objects.all()
    return render(request, 'show.html', {'shoes': shoes})

def edit(request, id):
    shoes = Products.objects.get(id=id)
    return render(request, 'edit.html', {'shoes': shoes})

def update(request, id):
    shoes = Products.objects.get(id=id)
    form = Products(request.POST, instance=shoes)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return redirect(request, 'edit.html', {'shoes': shoes})

def destory(request, id):
    shoes = Products.objects.get(id=id)
    shoes.delete()
    return redirect('/show')

