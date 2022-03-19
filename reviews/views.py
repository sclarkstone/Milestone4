from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    """ Display the selected product to review """
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = UserReviewForm()

    product = get_object_or_404(Product, pk=product_id)
    order = get_object_or_404(Order, order_number=order_number)

    template = 'reviews/review_detail.html'
    context = {
        'form': form,
        'order': order,
        'product': product,
    }

    return render(request, template, context)
    

@login_required
def add_review(request):
    """ Add a user review """
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = UserReviewForm()
        
    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)