from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse


from .models import Order, OrderItem

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'viber', 'city', 'posta',
                    'sklad', 'paid', 'created', 'updated',]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInLine]

def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('orders:admin_order_pdf', args=[obj.id])))
order_pdf.short_description = 'Invoice'

#@admin.register(Order)
#class OrderAdmin(admin.ModelAdmin):
#    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'viber', 'city', 'posta',
#                    'sklad', 'paid', 'created', 'updated', 'order_pdf']
#    list_filter = ['paid', 'created', 'updated']


