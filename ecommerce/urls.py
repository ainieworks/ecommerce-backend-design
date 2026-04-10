from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Connect store app URLs to main project
    path('', include('store.urls')),
]