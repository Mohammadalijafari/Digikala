from .models import Product, Comment
from django.shortcuts import get_object_or_404, render, redirect
from .utils import get_product_last_price_list


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
    seller_prices = get_product_last_price_list(product_id)
    context = {
        'product': product,
        'seller_prices': seller_prices,
        'comments_count': product.product_comments.count()
    }
    return render(
        request=request,
        template_name="products/product_detail.html",
        context=context
    )


def create_comment(request, product_id):
    if request.method == 'POST':
        comment = Comment.objects.create(
            user_email=request.POST.get('user_email', None),
            title=request.POST.get('title', None),
            text=request.POST.get('text', None),
            rate=int(request.POST.get('rate', 0)),
            product_id=request.POST.get('product_id', None),
        )
        return redirect('products:product_detail', product_id=product_id)
