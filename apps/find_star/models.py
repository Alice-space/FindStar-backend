from django.db import models
from django.utils.translation import gettext_lazy as _


class Birth(models.Model):
    birth = models.DateField(verbose_name=_("birth"), unique=True)
    word = models.TextField(verbose_name=_("statement"))

    class Meta:
        verbose_name = _("Birth")
        verbose_name_plural = _("Births")

    def __str__(self):
        return self.birth.isoformat()


class Image(models.Model):
    birth = models.ForeignKey(Birth, on_delete=models.SET_NULL, null=True, blank=True)
    url = models.URLField(verbose_name=_('image url'))

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
