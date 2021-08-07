from ckeditor.fields import RichTextField
from django.db.models import (
    CharField,
    ForeignKey,
    ImageField,
    Model,
)
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


class SubMenu(Model):
    sub_menu = CharField(
        verbose_name=_("تایتل زیر مجموعه"), max_length=100, help_text=_("تایتل منو")
    )

    def __str__(self) -> str:
        return str(self.sub_menu)

    class Meta:
        verbose_name = _("چند منویی")
        verbose_name_plural = _("چند منویی ها")


class AbstractPage(Model):
    title = CharField(
        verbose_name=_("تایتل"), max_length=255, help_text=_("تایتل صفحه")
    )
    image = ImageField(verbose_name=_("عکس"), upload_to="page_uploads/", blank=True)
    content = RichTextField("متن")

    class Meta:
        abstract = True


class SubMenuPage(AbstractPage):
    sub_menu = ForeignKey(SubMenu, on_delete=CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("صفحه")
        verbose_name_plural = _("صفحه هات")


class Menu(AbstractPage):
    menu_title = CharField(
        verbose_name=_("تایتل منو"), max_length=100, help_text=_("Name of the Menu")
    )

    def __str__(self) -> str:
        return str(self.menu_title)

    class Meta:
        verbose_name = _("تک لینک")
        verbose_name_plural = _("تک لینک ها")
