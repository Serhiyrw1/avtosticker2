from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        ordering = ('name',)
        index_together = (('parent', 'slug'),)
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i + 1]))
        return slugs

    def __str__(self):
        return self.name





    def get_absolute_url(self):
        return reverse('shop:category_list', kwargs={ "category_slug": self.slug})

class Product(models.Model):
    category = TreeForeignKey(Category,
                                 related_name="products",
                                 on_delete=models.CASCADE,
                                 verbose_name = 'Категорія')
    name = models.CharField(max_length=200, db_index=True, verbose_name = 'Назва товару')
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name = 'Зображення')
    description = models.TextField(blank=True, verbose_name = 'Опис товару')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name = 'Ціна')
    avialable = models.BooleanField(default=True, verbose_name = 'Наявність продукту')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата створення')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Дата останнього редагування')
    views = models.IntegerField(default=0, verbose_name = 'Кількість переглядів')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'pk':self.id, 'slug':self.slug})
