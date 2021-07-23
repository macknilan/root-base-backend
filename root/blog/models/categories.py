""" Categories for the Blog """

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """Category model"""

    name = models.CharField(
        _("category name"), max_length=100, unique=True, help_text=_("Category name")
    )

    # class Meta:
    #     ordering = ("name",)

    def __str__(self):
        return self.name