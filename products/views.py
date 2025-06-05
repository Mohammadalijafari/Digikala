from .models import Product, Comment, Category
from django.shortcuts import get_object_or_404, render, redirect
from products.forms import ProductCommentModelForm


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


def product_detail_view(request, pk):
    p = get_object_or_404(Product.objects.select_related(
        'category').prefetch_related("product_comments"), pk=pk)

    if request.method == "GET":
        form = ProductCommentModelForm(initial={'product': p})
    elif request.method == 'POST':
        form = ProductCommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('products:product_detail', pk=pk)
    context = {
        "default_product_seller": p.sellers_last_prices[0],
        "product": p,
        "product_sellers": p.sellers_last_prices,
        "comments": p.product_comments.all(),
        "comment_counts": p.product_comments.all().count(),
        'comment_form': form
    }
    return render(
        template_name='products/product_detail.html',
        request=request,
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
    return None


def home(request):
    query = Product.objects.all()
    most_off_products = query
    most_sell = query
    most_recent = query
    context = {
        "most_off_products": most_off_products,
        "most_sell": most_sell,
        "most_recent": most_recent,
        "banners": [],
    }

    return render(
        template_name='products/index.html',
        request=request,
        context=context
    )


def category_view(request, category_slug):
    pass


def brand_view(request, category_slug):
    pass
