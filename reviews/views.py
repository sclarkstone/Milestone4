from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import UserReviewForm
from django.db.models import Avg


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



def review_detail(request, product_id):
    """ Display the selected product to review """
    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.filter(product_id=product_id).order_by('-date')
    review_total = Review.objects.filter(product_id=product_id).count()
    review_sum = Review.objects.filter(product_id=product_id).aggregate(Avg('rating'))['rating__avg']

    template = 'reviews/review_detail.html'
    context = {
        'product': product,
        'review': review,
        'review_total': review_total,
        'review_sum': review_sum,
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """ Add a user review """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            form.instance.user = profile.user
            form.instance.product_id = '8'
            form.instance.order_number = '8dsfdsfr34rfesd'
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
        'profile': profile,
        'product_id': product_id,
    }

    return render(request, template, context)


@login_required
def delete_review(request, product_id, order_number):
    """ Delete a review """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, product_id=product_id, order_number=order_number)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('reviews'))