from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('<int:product_id>/<order_number>/', views.review_detail, name='review_detail'),
    path('add/', views.add_review, name='add_review'),
]
