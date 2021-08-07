from django.test import TestCase
from .models import NewsPost


class NewsPostModelTest(TestCase):
    def test_get_time(self):
        d = NewsPost.objects.all().first()
        self.assertIs(d.get_time(), str)
