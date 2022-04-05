from django.shortcuts import render, get_object_or_404
from collections import defaultdict
from django.core.exceptions import PermissionDenied


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
    profile_name = get_object_or_404(UserProfile, user=request.user)

    profile = get_object_or_404(Product, pk=product_id)
    distance = get_object_or_404(Distance, product_id=product_id)
    
    orders = profile_name.orders.all()
    order_item = Order.objects.filter(user_profile=request.user.userprofile)
    order_items = OrderLineItem.objects.filter(order__user_profile=request.user.userprofile, product=product_id).values_list('product')

    if not order_items:
        profile = get_object_or_404(Product, pk=False)
   
    session = Session.objects.filter(distance=distance.pk)
    daynames = {'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5, 'Saturday' : 6, 'Sunday' : 7}

    days = {1,2,3,4,5,6,7}
    session_dict = defaultdict(list)

    for week, day in session.values_list('week', 'day'):
        session_dict[week].append(day)
    


    context = {
        'profile': profile,
        'session': session,
        'distance': distance,
        'duration': range(1,int(distance.duration)+1),
        'days': days,
        'daynames': daynames,
        'session_dict': dict(session_dict),
        'order_item': order_item,
        'orders': orders,
        'order_items': order_items,
        'order_item': order_items,
        'plans': plans,



    }

    return render(request, 'plans/plan_detail.html', context)
