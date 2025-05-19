from django.contrib import admin
from .models import Product, Category, Comment, Question, Answer, Image, ProductOption, SellerProductPrice, Brand


# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1


class ProductPriceInLine(admin.TabularInline):
    model = SellerProductPrice
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'english_name', 'name', 'category']
    list_filter = ['category']
    search_fields = ['name', 'english_name']
    inlines = (ProductImageInline, ProductOptionInline, ProductPriceInLine)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'parent']
    list_filter = ['parent']
    search_fields = ['name', 'description']
    fieldsets = [
        ("Details", {'fields': ['name', 'slug', 'parent', 'description']}),
        ("Image", {'fields': ['icon', 'image']}),
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_email', 'product', 'title', 'rate']
    list_filter = ['product']
    search_fields = ['email', 'product']
    fieldsets = [
        ("Details", {'fields': ['title', 'text', 'rate']}),
        ("Product", {'fields': ['product']}),
        ("Writer", {'fields': ['user_email']}),
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_email', 'product', 'text']
    list_filter = ['product', 'user_email']
    search_fields = ['user_email', 'product']
    fieldsets = [
        ("Question", {'fields': ['text']}),
        ("Product", {'fields': ['product']}),
        ("Writer", {'fields': ['user_email']}),
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'text']
    list_filter = ['question']
    search_fields = ['question']
    fieldsets = [
        ("Answer", {'fields': ['text']}),
        ("Question", {'fields': ['question']}),
    ]


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'name', 'value']
    list_filter = ['product', 'name']
    search_fields = ['name', 'value', 'product']
    fieldsets = [
        ("Product", {'fields': ['product']}),
        ("Option", {'fields': ['name', 'value']}),
    ]


@admin.register(SellerProductPrice)
class SellerProductPriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'price', 'create_at', 'update_at']
    list_filter = ['product']
    search_fields = ['product']
    fieldsets = [
        ("Product", {'fields': ['product']}),
        ("Price", {'fields': ['price']}),
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
