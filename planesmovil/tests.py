from django.test import TestCase
from .models import Plan_movil
from django.contrib.auth.models import User


class PlanmovilTestCase(TestCase):
    def setUp(self):
        userCreate = User.objects.create(
            username='admin',
            password='admin',
            email='admin@admin.cl'
        )
        Plan_movil.objects.create(
            title="Plan 18GB",
            precio=13000,
            description="500 min + 100 SMS",
            publishedBy=userCreate,
            views=100)
        Plan_movil.objects.create(
            title="Plan 30 GB",
            precio=18000,
            description="900 min + 100 SMS",
            publishedBy=userCreate,
            views=500)

    def test_count_views(self):
        Plan18 = Plan_movil.objects.get(title="Plan 18GB")

        self.assertEqual(Plan18.views, 100)
    def test_precio(self):
        Plan18 = Plan_movil.objects.get(title="Plan 18GB")

        self.assertEqual(Plan18.precio, 13000)