from django.shortcuts import render


def products_home(request):
    template_name = 'products/products_home.html'
    return render(request, template_name)


def about_product(request):
    template_name = 'products/about_product.html'
    return render(request, template_name)


def all_products(request):
    template_name = 'products/all_products.html'
    return render(request, template_name)

def popular_products(request):
    template_name = 'products/popular_products.html'
    return render(request, template_name)


def new_products(request):
    template_name = 'products/new_products.html'
    return render(request, template_name)