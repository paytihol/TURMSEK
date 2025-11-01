from django.db import models
from django.utils.translation import gettext_lazy as _






class Item(models.Model):
    class Meta:
        verbose_name = _('мой тунк')
        verbose_name_plural = _('мои тунчеки')
    IsTurmsek = models.BooleanField(
        _('турмс или не турмс вот в чем вопрос'), default=False)
    title = models.CharField(_('Название'), max_length=999)
    tankType = models.CharField(_('тип тунка'), max_length=99)
    OnoTogoStoit = models.BooleanField(_('стоит ли брать'), default=False)
    date = models.DateField(_('дата выхода танка в реальности'))
    IsPonerflenVHlam = models.BooleanField(
        _('Понерфлен ли улиткой в хлам'), default=True)
    description = models.CharField(_('опИсание'), max_length=9999)
    cost = models.DecimalField(
        _('ценна в рублях'), max_digits=15, decimal_places=2)
    stock = models.IntegerField(_('количество пакетиков с танком'), default=0)
    image = models.ImageField(upload_to='imgs/', null= True, default= "imgs/default.png")

    def __str__(self):
        return self.title
