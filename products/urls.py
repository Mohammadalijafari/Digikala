from .views import product_detail_view, product_list_view, create_comment, home, brand_view, category_view
from django.urls import path

app_name = "products"
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('<int:pk>/', product_detail_view, name='product_detail'),
    path('brand/<slug:brand_slug>/', brand_view, name='brand_detail'),
    path('category/<slug:category_slug>/', category_view, name='category_detail'),
]
