from .views import product_single_view, product_list_view
from django.urls import path

app_name = "products"
urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<int:product_id>/', product_single_view, name='product_single'),
]
