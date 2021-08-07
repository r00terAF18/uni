from django.db.models import (
    BooleanField,
    CharField,
    ForeignKey,
    ImageField,
    Model,
)
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


class Carousel(Model):
    carousel_title = CharField(
        verbose_name=_("نام سلایدر"), max_length=100, default=_("سلایدر")
    )
    is_active = BooleanField(
        verbose_name=_("فعال شود؟"),
        help_text=_("اگر تیک شود قابل مشاهده برای همه خواهد بود"),
        default=True,
    )

    def __str__(self) -> str:
        return str(self.carousel_title)

    class Meta:
        verbose_name = "سلایدر"
        verbose_name_plural = "سلایدر ها"


class CarouselItem(Model):
    item_carousel = ForeignKey(Carousel, on_delete=CASCADE)
    img = ImageField(_("عکس"), default="", upload_to="carousel/", blank=True, null=True)
    details = CharField(_("متن"), max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f"Carouself item of {self.item_carousel}"

    class Meta:
        verbose_name = _("سلایدر")
        verbose_name_plural = _("سلایدر ها")
