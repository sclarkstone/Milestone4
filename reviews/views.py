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
def my_reviews(request):
    """ display user reviews"""
    profile = get_object_or_404(UserProfile, user=request.user)
    
    review_completed = Review.objects.filter(user=request.user.userprofile)
    products = Product.objects.all()

    review_complete_product = Review.objects.filter(user=request.user.userprofile).values('product_id')
    review_complete_order = Review.objects.filter(user=request.user.userprofile).values('order_number')
    reviews_needed = OrderLineItem.objects.filter(order__user_profile=request.user.userprofile).exclude(product__pk__in=review_complete_product, order__order_number__in=review_complete_order).all()

    template = 'reviews/my_reviews.html'
    context = {
        'profile': profile,
        'products': products,
        'review_completed': review_completed,
        'reviews_needed': reviews_needed,
        'review_complete_product': review_complete_product,
        'review_complete_order': review_complete_order,
    }
    

    return render(request, template, context)



def review_detail(request, product_id):
    """ Display the selected product to review """
    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.filter(product_id=product_id).order_by('-date')
    review_total = Review.objects.filter(product_id=product_id).count()
    
    if review_total == 0:
        review_sum = 0
    else:
        review_sum = Review.objects.filter(product_id=product_id).aggregate(Avg('rating'))['rating__avg']
 
    template = 'reviews/review_detail.html'
    context = {
        'product': product,
        'review': review,
        'review_total': review_total,
        'review_sum': (round(review_sum, 1)),
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id, order_number):
    """ Add a user review """
    order = get_object_or_404(Order, order_number=order_number)
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            form.instance.user = profile
            form.instance.product_id = product.id
            form.instance.order_number = order.order_number
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('my_reviews'))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = UserReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'profile': profile,
        'product': product,
        'order': order,
    }

    return render(request, template, context)


@login_required
def delete_review(request, product_id, order_number):
    """ Delete a review """

    review = Review.objects.filter(product_id=product_id, order_number=order_number).first()
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('my_reviews'))


@login_required
def edit_review(request, product_id, order_number):
    """ Edit a review """
    review = Review.objects.filter(user=request.user.userprofile, product_id=product_id, order_number=order_number).first()
    order = get_object_or_404(Order, order_number=order_number)
    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('my_reviews'))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = UserReviewForm(instance=review)
        messages.info(request, f'You are editing review for {product.name}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'product': product,
        'profile': profile,
        'order': order,
    }

    return render(request, template, context)
