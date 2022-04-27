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
def my_plans(request):
    """ display users plans"""
    profile = get_object_or_404(UserProfile, user=request.user)

    order_items = OrderLineItem.objects.filter(order__user_profile=request.user.userprofile, product__category=5)

    template = 'plans/my_plans.html'
    context = {
        'profile': profile,
        'order_items': order_items,
    }
    
    return render(request, template, context)

@login_required
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
    session_list_by_day = []
    days_list = [1,2,3,4,5,6,7]
    days_map = {1,2,3,4,5,6,7}

    weeks = range(1,int(distance.duration)+1)
    days = range(1,int(7)+1)

    for counter_week, duration in enumerate(weeks, start=1):
        for counter_day, day in enumerate(days, start=1):
            session_for_day = Session.objects.filter(day=counter_day, week=counter_week, distance__product_id=product_id).values('description', 'effort', 'day', 'week')
            if not session_for_day:
                session_for_day = list([{'description': 'REST', 'day': counter_day, 'week': counter_week}])
                session_list_by_day += session_for_day
            else:
                session_for_day = list(session_for_day)
                session_list_by_day += session_for_day

        session_list_by_day += session_for_day
            

    weeks = Distance.objects.filter(product_id=product_id)

    context = {
        'profile': profile,
        'session': session,
        'distance': distance,
        'duration': range(1,int(distance.duration)+1),
        'days': days_map,
        'daynames': daynames,
        'order_item': order_item,
        'orders': orders,
        'order_items': order_items,
        'order_item': order_items,
        'weeks': weeks,
        'session_list_by_day': session_list_by_day
    }

    return render(request, 'plans/plan_detail.html', context)