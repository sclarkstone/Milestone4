from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_reviews, name='my_reviews'),
    path('<int:product_id>/', views.review_detail, name='review_detail'),
    path('add/<int:product_id>/<str:order_number>',
         views.add_review,
         name='add_review'),
    path('edit/<int:product_id>/<str:order_number>',
         views.edit_review,
         name='edit_review'),
    path('delete/<int:product_id>/<str:order_number>',
         views.delete_review,
         name='delete_review'),
]
