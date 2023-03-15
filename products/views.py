from django.shortcuts import render, redirect
from products.forms import ProductsForm
from products.models import Products, ProductAdmin
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

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

def checkout(request, id):
    shoes = Products.objects.get(id=id)
    return render(request, 'checkout.html', {'shoes':shoes})

def payment(request, id):
    products = Products.objects.get(id=id)
    if request.method == 'POST':
        amount = Products.Product_price
        phonenumber = request.POST.get('phonenumber')
        if not phonenumber or not phonenumber.isdigit:
            return HttpResponse('phone number invalid!')
        if not amount or not amount.isdigit:
            return HttpResponse('amount is invalid!')

        cl = MpesaClient()
        phone_number = int(phonenumber)
        account_reference = 'VIATU ENTERPRISES'
        transaction_desc = 'Payment for shoes'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(phone_number, account_reference, transaction_desc,callback_url)
        return HttpResponse(response)
    else:
        return render(request, 'checkout.html', {'products':products})

def Admindisplay(request):
    productadmin = ProductAdmin.objects.all()
    return render(request, 'admindisplay.html', {'productadmin':productadmin})

def Admincheckout(request, id):
    productadmin = ProductAdmin.objects.get(id=id)
    return render(request, 'admincheckout.html', {'productadmin':productadmin})

def checkoutpayment(request, id):
    productadmin = ProductAdmin.objects.get(id=id)
    if request.method == 'POST':
        amount = ProductAdmin.Product_price
        phonenumber = request.POST.get('contact')
        if not phonenumber or not phonenumber.isdigit:
           return HttpResponse('phone number is invalid!')
        if not amount or not amount.isdigit:
            return HttpResponse('Amount is invalid!')

        cl = MpesaClient()
        phone_number = int(phonenumber)
        amount = int(amount)
        account_reference = 'VIATU ENTERPRISES'
        transaction_desc = 'Payment for shoes'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(str(phone_number), amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    else:
          return render(request, 'admincheckout.html', {'products':products})





def destory(request, id):
    shoes = Products.objects.get(id=id)
    shoes.delete()
    return redirect('/show')

