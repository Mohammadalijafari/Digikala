from .views import index, product_view
from django.urls import path

urlpatterns = [
    path('', index),
    path('<int:product_id>/', product_view),
]
