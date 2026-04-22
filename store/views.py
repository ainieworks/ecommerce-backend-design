from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product
from .forms import ProductForm


# ── HOME ──────────────────────────────────────────────────────
def home(request):
    # Only show in-stock products as featured — max 4
    featured_products = Product.objects.filter(stock__gt=0)[:4]
    context = {
        'products': featured_products,
    }
    return render(request, 'home.html', context)


# ── PRODUCT LIST WITH SEARCH AND PAGINATION ───────────────────
def product_list(request):
    from django.core.paginator import Paginator

    query = request.GET.get('q', '').strip()
    page_number = request.GET.get('page', 1)

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        ).order_by('name')
    else:
        products = Product.objects.all().order_by('name')

    # 9 products per page
    paginator = Paginator(products, 9)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'products.html', context)


# ── PRODUCT DETAIL ────────────────────────────────────────────
def product_detail(request, id):
    # Returns 404 if product not found — never crashes
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)


# ── ADD PRODUCT — login required ──────────────────────────────
@login_required
def add_product(request):
    if request.method == 'POST':
        # request.FILES needed for image upload
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


# ── LOGIN ─────────────────────────────────────────────────────
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# ── SIGNUP ────────────────────────────────────────────────────
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# ── LOGOUT ────────────────────────────────────────────────────
def logout_view(request):
    logout(request)
    return redirect('home')

