from django import forms

from products.models import Comment, Product


# we use this kind of forms just when we are not dealing with models
# class ProductCommentForm(forms.Form):
#     user_email = forms.EmailField(
#         label="ایمیل",
#         widget=forms.EmailInput(attrs={'class': 'form-control'})
#     )
#     title = forms.CharField(
#         max_length=150, label="عنوان",
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#     text = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control'}),
#         label="متن نظر",
#     )
#     rate = forms.IntegerField(
#         label="امتیاز",
#         widget=forms.NumberInput(attrs={'class': 'form-control'})
#     )
#     product_id = forms.IntegerField(widget=forms.HiddenInput)
#
#     def clean_product_id(self):
#         product_id = self.cleaned_data['product_id']
#         query = Product.objects.filter(id=product_id)
#         if not query.exists():
#             raise forms.ValidationError("Invalid product id")
#         return product_id


class ProductCommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'product': forms.HiddenInput()
        }

    def save(self, commit: bool = ...):
        return super().save(commit)
