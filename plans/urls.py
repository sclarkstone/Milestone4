from django.urls import path
from . import views

urlpatterns = [
    path('', views.plans, name='plans'),
    path('<int:product_id>/', views.plan_detail, name='plan_detail'),
]
