from django.db.models import (
    CharField,
    ImageField,
    Model,
)
from django.db.models.fields import URLField
from django.utils.translation import gettext_lazy as _

# UNIVERSITY SYSTEM STUFF


class UniSystem(Model):
    uni_system_title = CharField(verbose_name=_("تایتل"), max_length=255)
    uni_system_link = URLField(verbose_name=_("لینک"), max_length=300)
    uni_system_image = ImageField(
        verbose_name=_("عکس"), default="", upload_to="uni_system_image/", blank=True
    )

    def __str__(self) -> str:
        return self.uni_system_title

    class Meta:
        verbose_name = _("سیستم دانشگاه")
        verbose_name_plural = _("سیستم های دانشگاه")
