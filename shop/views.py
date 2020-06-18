from django.shortcuts import render, get_object_or_404
from django.template import loader, Context, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.http import Http404, HttpResponse

from .models import Category, Product
from cart.forms import CartAddProductForm

def test(request):
    return render(request, "shop/home.html", {'categories': Category.objects.all()})


def product_list(request):
    def product(request,  slug):
        product = get_object_or_404(Product,  slug=slug)
#        cart_product_form = CartAddProductForm()
        categories = Category.objects.all()
        return render(request, 'shop/category_list.html',
                      {'product': product,
 #                      'cart_product_form': cart_product_form,
                       'categories': categories,
                       })




def category_list_child(request, slug = None):
    category = get_object_or_404(Category, slug=slug)
#    category = Category.objects.get(pk = category_id)

    products = Product.objects.filter(category__slug=slug)

#    category = get_object_or_404(Category, pk = category_id)
#    if pk:
#        category = get_object_or_404(Category, pk = pk)
#        products = Product.objects.filter(category= category)

    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:

        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/category_list_child.html',
                  {'category': category,
                   'products':products,
                   'page':page

                   })

def category_list(request, category_id):
    category = Category.objects.get_children(pk=category_id)

    products = Product.objects.filter(category_id=category_id)

 #   parent_primary_keys = Category.objects.filter(pk = root_category_id).values_list('pk', flat=True)

#    products = Product.objects.filter(id__in=parent_primary_keys)



 #   category = Category.objects.get(slug = category_slug)
 #   products = Product.objects.filter(category= category)

 #   category = Category.objects.get(id=category_id)
 #   root_category_id = category.get_root().id

#    pr = Product.objects.all()
#    products = pr.filter(category_id=root_category_id)



#    category = get_object_or_404(Category, pk = category_id)
#    if pk:
#        category = get_object_or_404(Category, pk = pk)
#        products = Product.objects.filter(category= category)

    return render(request, 'shop/category_list.html',
                  {'nodes':Category.objects.all(),
 #                             'category':category,
  #                            'categories': categories,

                   'products': products,


                   })


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, pk=pk,  slug=slug)
 #   category = get_object_or_404(Category, slug=slug)
    cart_product_form= CartAddProductForm()
    categories = Category.objects.all()
    return render(request, 'shop/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                    'categories':categories,
#                   'category': category
                   })

def show_category(request,  slug ):
    category_slug = slug.split('/')
    parent = None
    root = Category.objects.all()

    for slug in category_slug:
        parent = root.get(parent=parent,  slug = slug)
#        products = get_object_or_404(Product, slug=category_slug[-1])
#        return render(request, 'shop/categories.html', {
#                                                        'products': products})
#        products = Product.objects.filter(category__slug=slug)

#    try:
#        instance = Category.objects.get(parent=parent,slug=category_slug[-1])

#    except:
    instance = get_object_or_404(Category, slug = category_slug[-1])
    products = Product.objects.filter(category__parent=parent)

    paginator = Paginator(products, 8)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:

        products = paginator.page(paginator.num_pages)
    return render(request, "shop/category_list.html", {'instance':instance,
                                                           'products': products,
                                                       'page':page})
#    else:
#        products = Product.objects.filter(slug='znaki')
#        return render(request, 'shop/base.html', {'instance':instance,
#                                                       'products':products })