from django.contrib import admin
from store.models import Event, Order, Cart, PromoCode

# Register your models here.

admin.site.register(Event)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(PromoCode)
