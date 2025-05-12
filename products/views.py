from .models import Product
from django.shortcuts import get_object_or_404, render


# Create your views here.
def product_list_view(request):
    page = int(request.GET.get('page', 1))
    page_size = 10
    query = Product.objects.all()
    q = request.GET.get('q', None)  # new

    if q:
        query = Product.objects.filter(name__icontains=q)

    products = query[page * page_size:(page + 1) * page_size]

    return render(request, 'products/product-list.html', context={'products': products})


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(
        request=request,
        template_name="products/product_detail.html",
        context=context
    )
