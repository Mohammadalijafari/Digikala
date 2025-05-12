from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.
class Seller(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    slug = models.SlugField(verbose_name=_("Slug"), max_length=255, unique=True)

    class Meta:
        verbose_name = _("Seller")
        verbose_name_plural = _("Sellers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
