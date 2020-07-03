from django.contrib import admin
# Register your models here.
from .models import product, ClientInfo, Order, OrderUpdate
admin.site.register(product)
admin.site.register(ClientInfo)
admin.site.register(Order)
admin.site.register(OrderUpdate)