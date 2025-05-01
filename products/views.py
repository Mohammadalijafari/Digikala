from .models import Category, Product
from django.shortcuts import HttpResponse, get_object_or_404, render


# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:10]
    return HttpResponse()


def product_view(request, product_id):
    p = get_object_or_404(Product, id=product_id)
    context = {'product': p}
    return render(
        request=request,
        template_name="products/product.html",
        context=context
    )
