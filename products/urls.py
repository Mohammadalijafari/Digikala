from .views import product_view, product_list_view
from django.urls import path

urlpatterns = [
    path('', product_list_view),
    path('<int:product_id>/', product_view),
]
