from core.models import Lecture, NewsPost, Event
from django.forms import ModelForm
from django.forms.fields import CharField, ImageField, URLField
from django.forms.widgets import FileInput, TextInput, URLInput, DateInput
from .models import UniSystem
from professor_app.models import ProfessorPost, ProfessorUpload, Departmant
from pages_app.models import SubMenu, SubMenuPage, Menu


class NewsForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = "__all__"
        exlude = ["draft", "STYLES", "date_created"]


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        # exlude = []
        widgets = {
            "event_date": DateInput(
                attrs={"type": "date", "class": "mt-4 inp font-weight-550 text-474747"}
            )
        }


class LectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = "__all__"
        exlude = ["draft", "STYLES", "date_created"]


class UniSystemForm(ModelForm):
    uni_system_title = CharField(
        max_length=255,
        required=True,
        label="نام سیستم",
        widget=TextInput(
            attrs={
                "class": "inp font-weight-550 text-black-50",
                "placeholder": "نام سیستم را وارد کنید",
            }
        ),
    )

    uni_system_link = URLField(
        max_length=300,
        required=True,
        label="لینک",
        widget=URLInput(
            attrs={
                "class": "inp font-weight-550 text-black-50",
                "placeholder": "لینک سیستم را وارد کنید",
            }
        ),
    )

    uni_system_image = ImageField(
        required=False, widget=FileInput(attrs={"accept": "image/*"})
    )

    class Meta:
        model = UniSystem
        fields = "__all__"


class DepForm(ModelForm):
    class Meta:
        model = Departmant
        fields = "__all__"


class ProfessorPostForm(ModelForm):
    class Meta:
        model = ProfessorPost
        fields = "__all__"


class ProfessorUploadForm(ModelForm):
    class Meta:
        model = ProfessorUpload
        fields = "__all__"


# PAGE


class PageForm(ModelForm):
    class Meta:
        model = SubMenuPage
        fields = "__all__"


# MENU
class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"


class SubMenuForm(ModelForm):
    class Meta:
        model = SubMenu
        fields = "__all__"


# class StudentPostFilter(django_filters.FilterSet):
#     # from_student = django_filters.ModelChoiceFilter() # lookup_expr='icontains', label="نام دانشجو"
#     date_created = django_filters.DateFromToRangeFilter(
#         label="تاریخ", widget=DateRangeWidget(attrs={"type": "date"})
#     )
#     title = django_filters.CharFilter(lookup_expr="icontains", label="نام پست")

#     class Meta:
#         model = StudentPost
#         fields = ["from_student", "title", "date_created"]


# class SelfPostFilter(django_filters.FilterSet):
#     date_created = django_filters.DateFromToRangeFilter(
#         label="تاریخ", widget=DateRangeWidget(attrs={"type": "date"})
#     )
#     title = django_filters.CharFilter(lookup_expr="icontains", label="نام پست")
#     draft = django_filters.BooleanFilter(label="وضعیت")

#     class Meta:
#         model = StudentPost
#         fields = ["title", "date_created", "draft"]
