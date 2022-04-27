from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_plans, name='my_plans'),
    path('<int:product_id>/', views.plan_detail, name='plan_detail'),
]
