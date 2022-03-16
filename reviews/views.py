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
    """ A view to show individual review details """

    profile = get_object_or_404(Product, pk=product_id)

    context = {
        'profile': profile,
    }

    return render(request, 'reviews/review_detail.html', context)
