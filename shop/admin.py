from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from .models import Category, Product

# admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
prepopulated_fields = {'slug': ('name',)},
)

#@admin.register(Category)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}