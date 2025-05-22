from products.models import SellerProductPrice


def get_product_last_price_list(product_id):
    return SellerProductPrice.objects.raw(
        f"""select * from products_sellerproductprice
        where product_id = {product_id}
        group by seller_id
        having max(update_at)""", {'id': product_id}
    )
