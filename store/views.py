from django.shortcuts import render

# Home page view
# When user visits /, Django calls this function
def home(request):
    return render(request, 'home.html')

# Product listing view
# When user visits /products/, Django calls this
def product_list(request):
    return render(request, 'products.html')

# Product detail view
# When user visits /products/1/, Django calls this
# id comes from the URL — tells us which product to show
def product_detail(request, id):
    return render(request, 'product_detail.html')