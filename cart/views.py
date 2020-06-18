from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.conf import settings

from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm


@require_POST

def cart_add(request, product_id ):
    cart=Cart(request)
    product= get_object_or_404(Product, id= product_id)
    form = CartAddProductForm(request.POST)


    if form.is_valid():
        cd = form.cleaned_data

        cart.add(product=product,
                 quantity=cd['quantity'],

                 update_quantity=cd['update'])


    return redirect('cart:cart_detail')

def cart_plus(request, product_id ):
    cart=Cart(request)
    product= get_object_or_404(Product, id= product_id)
    form = CartAddProductForm(request.POST)
    cart.plus(product=product,
                 quantity=['quantity'],
                 plus=['plus'],
                 )
    return redirect('cart:cart_detail')

def cart_minus(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    cart.minus(product=product,
              quantity=['quantity'],
              minus=['minus'],
              )
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_del(request):
    cart = Cart(request)
    del cart.session[settings.CART_SESSION_ID]
    cart.save()
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart=Cart(request)
    categories = Category.objects.all()
    for item in cart:

        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'plus': True,
                     'minus': True,
                     'update': True,
                     }
        )

    return render(request, 'cart/detail.html', {'cart': cart,
                                                'categories': categories,

                                                 })