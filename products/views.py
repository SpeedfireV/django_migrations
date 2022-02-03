from django.shortcuts import render, redirect
from products import models
from products.forms import ProductForm
from products.models import Category, Product, Order, ProductType
from django import forms
from django.http import Http404, HttpResponseRedirect


def home(request):
    category_list = Category.objects.all()
    return render(request, 'home.html', {
        "categories": category_list,
    })

def category_view(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        print(f'{category=}')
        products = Product.objects.filter(category=category)
    except Category.DoesNotExist or Product.DoesNotExist:
        raise Http404


    return render(request, "category.html", {
        "products": products,
        "category": category,
    })

def product_view(request, product_id):
    print('wchodzi na strone produktu o id=', product_id)

    # pozyskaj Product o podanym product_id lub zwroc blad 404
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404

    # pozyskaj wszystkie product_type nalezace do product

    form = ProductForm(request.POST or None, product=product)
    if form.is_valid():
        color = form.cleaned_data.get("color")
        return redirect('order', product.id, color)

    return render(request, 'product.html', {
        "form": form,
        "product": product,
    })

def order_view(request, product_id, color):


    try:
        product = Product.objects.get(id=product_id)
        product_types = ProductType.objects.filter(product=product)
    except Product.DoesNotExist or ProductType.DoesNotExist:
        raise Http404


    surname = request.POST.get("surname")

    colors = ()
    for product_type in product_types:
        colors += (product_type.color, )

    return render(request, 'order.html', {
            "product" : product,
            "product_types" : product_types,
            "color": color,

    })

# Create your views here.
