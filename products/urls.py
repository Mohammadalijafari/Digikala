from .views import product_detail_view, product_list_view, create_comment
from django.urls import path

app_name = "products"
urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<int:product_id>/', product_detail_view, name='product_detail'),
    path('<int:product_id>/comments/', create_comment, name='create_comment'),
]
