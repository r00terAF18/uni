from django.db.models import (
    BooleanField,
    CharField,
    ForeignKey,
    Model,
    SlugField,
)
from django.db.models.deletion import CASCADE
from django.db.models.fields import URLField
from django.utils.translation import gettext_lazy as _


class Sidebar(Model):

    FOR_PAGE = (
        ("Daneshkadeh", "دانشکده"),
        ("Ostad", "استاد"),
        ("Lecture", "آموزش"),
        ("News", "اخبار"),
    )

    sidebar_title = CharField(verbose_name=_("تایتل"), max_length=255)
    sidebar_on_page = CharField(
        verbose_name=_("صفحه"),
        help_text=_("صفحه ای که سایدبار نشان داده شود"),
        choices=FOR_PAGE,
        max_length=15,
    )
    sidebar_is_active = BooleanField(verbose_name=_("سایدبار فعال باشد؟"), default=True)

    def __str__(self) -> str:
        return str(self.sidebar_title)

    class Meta:
        verbose_name = _("سایدبار")
        verbose_name_plural = _("سایدبار ها")


class SidebarItem(Model):
    sidebar = ForeignKey(Sidebar, on_delete=CASCADE)
    sidebar_item_title = CharField(
        verbose_name=_("تایتل"),
        max_length=255,
        unique=False,
    )
    sidebar_link = SlugField(verbose_name=_("لینک"), allow_unicode=True, unique=False)

    def __str__(self) -> str:
        return str(self.sidebar_item_title)
