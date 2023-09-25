from django.contrib import admin
from .models import Category, Flower, Orders, Cart, Payment, UserDetails
# Register your models here.

admin.site.register(Flower)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(UserDetails)
admin.site.register(Orders)