from .models import Product
from django.shortcuts import get_object_or_404, render


# Create your views here.
def product_list_view(request):
    products = Product.objects.all()

    return render(request, 'products/product_list.html', context={'products': products})


def product_view(request, product_id):
    p = get_object_or_404(Product, id=product_id)
    context = {'product': p}
    return render(
        request=request,
        template_name="products/product_single.html",
        context=context
    )
