from django.shortcuts import render, redirect

from .forms import CreateProductForm

from .models import Products


def home():
    pass

def detailProduct(request, p_id):
    product = Products.objects.get(pk=p_id)

    return render(request, 'product-detail.html', {'product':product})

def deleteProduct(request, p_id):
    product = Products.objects.get(pk=p_id)
    product.delete()

    return redirect('home')

def createProduct(request):
    form = CreateProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'create-product.html', {'form':form})

