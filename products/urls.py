from .views import product_detail_view, product_list_view
from django.urls import path

app_name = "products"
urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<int:product_id>/', product_detail_view, name='product_detail'),
]
