from django.contrib import admin
from pharmacy.models import Medicine, Prescription, Cart, Order

admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(Cart)
admin.site.register(Order)
