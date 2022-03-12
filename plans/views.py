from django.shortcuts import render, get_object_or_404
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Session

from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from products.models import Product, Category


@login_required
def plans(request):
    """ display users plans"""
    profile = get_object_or_404(UserProfile, user=request.user)

    categories = Product.objects.filter(category=5).values_list('name')

    orders = profile.orders.all()

    template = 'plans/plans.html'
    context = {
        'profile': profile,
        'orders': orders,
        'categories': categories,
    }
    

    return render(request, template, context)


def plan_detail(request, product_id):
    """ A view to show individual plan details """

    profile = get_object_or_404(Product, pk=product_id)
    session = Session.objects.all()


    context = {
        'profile': profile,
        'session': session,
    }

    return render(request, 'plans/plan_detail.html', context)
