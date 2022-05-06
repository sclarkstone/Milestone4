from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Session, Distance

from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from products.models import Product


@login_required
def my_plans(request):
    """ display users plans"""
    profile = get_object_or_404(UserProfile, user=request.user)

    # get all items order by user that are a plan (category 5)
    order_items = OrderLineItem.objects.filter(
        order__user_profile=request.user.userprofile, product__category=5)

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

    # get all order for user
    orders = profile_name.orders.all()
    order_item = Order.objects.filter(user_profile=request.user.userprofile)

    # get all user order items
    order_items = OrderLineItem.objects.filter(
        order__user_profile=request.user.userprofile,
        product=product_id).values_list('product')

    # check the user has purcased the selected plan
    if not order_items:
        messages.error(request, 'Sorry, you have not purchased this plan.')
        order_items = OrderLineItem.objects.filter(
            order__user_profile=request.user.userprofile, product__category=5)
        template = 'plans/my_plans.html'
        context = {
            'profile': profile_name,
            'order_items': order_items,
        }

        return render(request, template, context)

    # get all sessions for selected plan
    session = Session.objects.filter(distance=distance.pk)

    # set up days of the week
    daynames = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3,
                'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    # initiate list for plan details to go into
    session_list_by_day = []

    # give the plans details page the day ids
    days_map = {1, 2, 3, 4, 5, 6, 7}

    # get the number of weeks for the selected plan, starting at 1
    weeks = range(1, int(distance.duration)+1)
    # get the number of days, starting at 1
    days = range(1, int(7)+1)

    # loop through the number of weeks in the selected plan
    for counter_week, duration in enumerate(weeks, start=1):
        # loop through the days of the week, for each week
        for counter_day, day in enumerate(days, start=1):
            # get session details for the day and week in the loop
            session_for_day = Session.objects.filter(
                day=counter_day,
                week=counter_week,
                distance__product_id=product_id).values(
                    'description',
                    'effort',
                    'day',
                    'week')
            # if there is not session details for the day the add default REST day
            if not session_for_day:
                session_for_day = list(
                    [{
                        'description': 'REST',
                        'day': counter_day,
                        'week': counter_week
                    }])
                session_list_by_day += session_for_day
            else:
                # if there are session details add them to the list
                session_for_day = list(session_for_day)
                session_list_by_day += session_for_day

        # pull together all session and default details for all
        # days of the week, for each week of the selected plan
        session_list_by_day += session_for_day

    weeks = Distance.objects.filter(product_id=product_id)

    context = {
        'profile': profile,
        'session': session,
        'distance': distance,
        'duration': range(1, int(distance.duration)+1),
        'days': days_map,
        'daynames': daynames,
        'orders': orders,
        'order_items': order_items,
        'order_item': order_items,
        'weeks': weeks,
        'session_list_by_day': session_list_by_day
    }

    return render(request, 'plans/plan_detail.html', context)
