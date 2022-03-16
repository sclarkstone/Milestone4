from django.shortcuts import render, get_object_or_404
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import UserReviewForm


from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from products.models import Product, Category


@login_required
def reviews(request):
    """ display user reviews"""
    profile = get_object_or_404(UserProfile, user=request.user)

    categories = Product.objects.filter(category=5).values_list('name')

    orders = profile.orders.all()
    
    template = 'reviews/reviews.html'
    context = {
        'profile': profile,
        'orders': orders,
        'categories': categories,
    }
    

    return render(request, template, context)


def review_detail(request, product_id, order_number):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserReviewForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review submitted successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserReviewForm(instance=profile)
    orders = profile.orders.all()

    template = 'reviews/review_detail.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)