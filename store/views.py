from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product


def home(request):
    # Only show in-stock products as featured
    featured_products = Product.objects.filter(stock__gt=0)[:4]
    context = {
        'products': featured_products,
    }
    return render(request, 'home.html', context)


def product_list(request):
    query = request.GET.get('q', '').strip()  # .strip() removes extra spaces

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        ).order_by('name')  # order results alphabetically
    else:
        products = Product.objects.all().order_by('name')

    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'products.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)