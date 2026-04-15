from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product


def home(request):
    # Show 4 products that are in stock for featured section
    featured_products = Product.objects.filter(stock__gt=0)[:4]
    context = {
        'products': featured_products,
    }
    return render(request, 'home.html', context)


def product_list(request):
    # Read search query from URL — e.g. /products/?q=phone
    query = request.GET.get('q', '')

    if query:
        # Search by name OR category — case insensitive
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )
    else:
        # No search — return all products
        products = Product.objects.all()

    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'products.html', context)


def product_detail(request, id):
    # If product doesn't exist — show 404 page, not crash
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)