from django.db import models

class Product(models.Model):
    # Name of the product
    name = models.CharField(max_length=200)

    # Long description text
    description = models.TextField()

    # Price — always use DecimalField for money, never float
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Category — Electronics, Fashion, Home, Sports, Books
    category = models.CharField(max_length=100)

    # Product image — stored in media/products/ folder
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    # Stock count — how many units available
    stock = models.IntegerField(default=0)

    # Auto-set when product is created
    created_at = models.DateTimeField(auto_now_add=True)

    # What shows in Django admin list
    def __str__(self):
        return self.name