from django.contrib import admin
from .models import cliente,Product,Category

# Register your models here.
admin.site.register(cliente)
admin.site.register(Product)
admin.site.register(Category)