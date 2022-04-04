from django.shortcuts import render, get_object_or_404
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Session, Distance

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
    distance = get_object_or_404(Distance, product_id=product_id)
    session = Session.objects.filter(distance=distance.pk)
    daynames = {'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5, 'Saturday' : 6, 'Sunday' : 7}

    context = {
        'profile': profile,
        'session': session,
        'distance': distance,
        'duration': range(1,int(distance.duration)+1),
        'days': [1,2,3,4,5,6,7],
        'daynames': daynames,
    }

    return render(request, 'plans/plan_detail.html', context)
