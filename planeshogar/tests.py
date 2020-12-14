from django.test import TestCase
from .models import Plan_hogar
from django.contrib.auth.models import User


class PlanhogarTestCase(TestCase):
    def setUp(self):
        userCreate = User.objects.create(
            username='admin',
            password='admin',
            email='admin@admin.cl'
        )
        Plan_hogar.objects.create(
            title="Plan Vive",
            precio=39990,
            description="200 Megas - 86 Canales + 71 HD - Telefonia ilimitada",
            publishedBy=userCreate,
            views=5000)
        Plan_hogar.objects.create(
            title="Plan Vive Pro",
            precio=59990,
            description="600 Megas - 91 Canales + 71 HD - Telefonia ilimitada",
            publishedBy=userCreate,
            views=7000)

    def test_count_views(self):
        PlanVive = Plan_hogar.objects.get(title="Plan Vive")

        self.assertGreaterEqual(PlanVive.views, 1000)
    def test_precio(self):
        PlanVivePro = Plan_hogar.objects.get(title="Plan Vive Pro")

        self.assertEqual(PlanVivePro.precio, 59990)