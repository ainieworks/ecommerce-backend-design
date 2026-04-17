from django.db import models


class Product(models.Model):
    # Short product name — max 200 characters
    name = models.CharField(max_length=200)

    # Full product description — no length limit
    description = models.TextField()

    # Price — DecimalField for precision, never use float for money
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Category — Electronics, Fashion, Home, Sports, Books
    category = models.CharField(max_length=100)

    # Optional product image — stored in media/products/ folder
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    # Available stock count
    stock = models.IntegerField(default=0)

    # Auto-set to current datetime when product is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Shows product name in Django admin list
        return self.name