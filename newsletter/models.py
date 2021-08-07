from ckeditor.fields import RichTextField
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import CharField, EmailField, Model
from django.utils.translation import gettext_lazy as _


class Subscriber(Model):
    email = EmailField(verbose_name=_("ثبت نام کننده"))
    # subscribed_to_newsletter = ForeignKey(Newsletter, on_delete=CASCADE)

    def __str__(self) -> str:
        return str(self.email)

    class Meta:
        verbose_name = _("ثبت نامی")
        verbose_name_plural = _("ثبت نامی ها")


class NewsletterMessage(Model):
    message_title = CharField(verbose_name=_("موضوع"), max_length=255)
    message_form = RichTextField(_("متن ایمیل"))

    def __str__(self) -> str:
        return str(self.message_title)

    def send_message(self):
        rec = Subscriber.objects.all()
        e_list = []
        for r in rec:
            e_list.append(str(r))

        send_mail(
            subject=self.message_title,
            message="message",
            html_message=self.message_form,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=e_list,
            fail_silently=False,
        )

    class Meta:
        verbose_name = _("ایمیل")
        verbose_name_plural = _("ایمیل ها")
