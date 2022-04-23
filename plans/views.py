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

    order_items = OrderLineItem.objects.filter(order__user_profile=request.user.userprofile, product__category=5)

    template = 'plans/plans.html'
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

    days = {1,2,3,4,5,6,7}
    
    weeks = range(1,int(distance.duration)+1)

    sessionListMonday = []
    sessionListTuesday = []
    sessionListWednesday = []
    sessionListThursday = []
    sessionListFriday = []
    sessionListSaturday = []
    sessionListSunday = []

    for counter, duration in enumerate(weeks, start=1):
        monday = Session.objects.filter(day=1, week=counter, distance__product_id=product_id).values('description', 'effort', 'day', 'week')
        tuesday = Session.objects.filter(day=2, week=counter, distance__product_id=product_id).values('description', 'effort', 'day', 'week')
        wednesday = Session.objects.filter(day=3, week=counter, distance__product_id=product_id).values('description', 'effort', 'day', 'week')
        thursday = Session.objects.filter(day=4, week=counter, distance__product_id=product_id).values('description', 'effort', 'day', 'week')
        friday = Session.objects.filter(day=5, week=counter, distance__product_id=product_id).values('description', 'effort', 'day', 'week')
        saturday = Session.objects.filter(day=6, week=counter, distance__product_id=product_id).values('description', 'effort', 'day', 'week')
        sunday = Session.objects.filter(day=7, week=counter, distance__product_id=product_id).values('description', 'effort', 'day', 'week')
        if not monday:
            MondayList = list([{'description': 'REST', 'day': 1, 'week': counter}])
        else:
            MondayList = list(monday)
        if not tuesday:
            TuesdayList = list([{'description': 'REST', 'day': 2, 'week': counter}])
        else:
            TuesdayList = list(tuesday)
        if not wednesday:
            WednesdayList = list([{'description': 'REST', 'day': 3, 'week': counter}])
        else:
            WednesdayList = list(wednesday)
        if not thursday:
            ThursdayList = list([{'description': 'REST', 'day': 4, 'week': counter}])
        else:
            ThursdayList = list(thursday)
        if not friday:
            FridayList = list([{'description': 'REST', 'day': 5, 'week': counter}])
        else:
            FridayList = list(friday)
        if not saturday:
            SaturdayList = list([{'description': 'REST', 'day': 6, 'week': counter}])
        else:
            SaturdayList = list(saturday)
        if not sunday:
            SundayList = list([{'description': 'REST', 'day': 7, 'week': counter}])
        else:
            SundayList = list(sunday)
        
        sessionListMonday += MondayList
        sessionListTuesday += TuesdayList
        sessionListWednesday += WednesdayList
        sessionListThursday += ThursdayList
        sessionListFriday += FridayList
        sessionListSaturday += SaturdayList
        sessionListSunday += SundayList    

    weeks = Distance.objects.filter(product_id=product_id)
    
    context = {
        'profile': profile,
        'session': session,
        'distance': distance,
        'duration': range(1,int(distance.duration)+1),
        'days': days,
        'daynames': daynames,
        'order_item': order_item,
        'orders': orders,
        'order_items': order_items,
        'order_item': order_items,
        'plans': plans,
        'weeks': weeks,
        'sessionListMonday': sessionListMonday,
        'sessionListTuesday': sessionListTuesday,
        'sessionListWednesday': sessionListWednesday,
        'sessionListThursday': sessionListThursday,
        'sessionListFriday': sessionListFriday,
        'sessionListSaturday': sessionListSaturday,
        'sessionListSunday': sessionListSunday,



    }

    return render(request, 'plans/plan_detail.html', context)
