from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@gmail.com",
            password="P@ssw0rd"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="Test@gmail.com",
            password="P@ssw0rd",
            name="Test User"
        )

    def test_user_listed(self):
        url = reverse('admin:account_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        url = reverse("admin:account_user_change", args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        url = reverse("admin:account_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
