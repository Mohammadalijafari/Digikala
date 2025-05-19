from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.
class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    english_name = models.CharField(_("English Name"), max_length=200)
    slug = models.SlugField(_("Slug"), max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class Product(models.Model):
    name = models.CharField(_("Persian Name"), max_length=200, )
    english_name = models.CharField(_("English Name"), max_length=200)
    description = models.TextField(_("Description"))
    category = models.ForeignKey(
        "Category",
        verbose_name=_("Category"),
        on_delete=models.PROTECT,
    )
    brand = models.ForeignKey(
        "Brand",
        verbose_name=_("Brand"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    sellers = models.ManyToManyField(
        "sellers.Seller",
        verbose_name=_("Sellers"),
        through="SellerProductPrice",
    )

    @property
    def default_image(self):
        return self.images.filter(is_default=True).first()

    @property
    def categories_list(self):
        categories_list = []
        current_category = self.category
        while current_category.parent is not None:
            categories_list.append(current_category)
            current_category = current_category.parent
        categories_list.append(current_category)
        return categories_list

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.id} {self.name}"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"), max_length=100, unique=True, db_index=True)
    description = models.TextField(_("Description"))
    icon = models.ImageField(_("Icon"), upload_to="category_images/", null=True, blank=True)
    image = models.ImageField(_("Image"), upload_to="category_images/", null=True, blank=True)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent Category"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.slug


class Comment(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    text = models.TextField(_("Text"))
    product = models.ForeignKey(
        "Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="product_comments",
    )
    rate = models.PositiveIntegerField(_("Rate"))
    user_email = models.EmailField(_("Email"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f'comment on {self.product.name}'


class Image(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    alt = models.CharField(_("Alternative Name"), max_length=100)
    product = models.ForeignKey(
        "Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(_("Image"), upload_to="products/")
    is_default = models.BooleanField(_("Is Default image"), default=False)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(_("Text"))
    user_email = models.EmailField(_("Email"))
    product = models.ForeignKey(
        "Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return f'Question about {self.product.name}'


class Answer(models.Model):
    text = models.TextField(_("Text"))
    question = models.ForeignKey(
        "Question",
        verbose_name=_("Question"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

    def __str__(self):
        return self.text


class ProductOption(models.Model):
    product = models.ForeignKey(
        'Product',
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="product_options",
    )
    name = models.CharField(_("Attribute"), max_length=200)
    value = models.CharField(_("Value"), max_length=200)

    class Meta:
        verbose_name = _("ProductOption")
        verbose_name_plural = _("ProductOptions")

    def __str__(self):
        return f'{self.product.name} {self.name}'


class SellerProductPrice(models.Model):
    product = models.ForeignKey(
        "Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="seller_prices",
    )
    seller = models.ForeignKey(
        "sellers.Seller",
        verbose_name=_("Seller"),
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField(_("Price"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(_("Update at"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Seller Product Price")
        verbose_name_plural = _("Seller Product Prices")

    def __str__(self):
        return f'{self.product.name} {self.price}'
