from django.test import TestCase
from django.urls import reverse

from comicsdb.models import Publisher
from users.models import CustomUser


class TestCaseBase(TestCase):

    def _create_user(self):
        user = CustomUser.objects.create(
            username='brian', email='brian@test.com')
        user.set_password('1234')
        user.save()

        return user

    def _client_login(self):
        self.client.login(username='brian', password='1234')


class PublisherUpdateTest(TestCaseBase):

    @classmethod
    def setUpTestData(cls):
        cls._create_user(cls)
        cls.dc = Publisher.objects.create(name='DC Comics', slug='dc-comics')

    def setUp(self):
        self._client_login()

    def test_publisher_update(self):
        resp = self.client.post(reverse('publisher:update',
                                        kwargs={'slug': self.dc.slug}),
                                {'name': 'DC Comics', 'slug': 'dc-comics', 'desc': 'Test data'})
        self.assertEqual(resp.status_code, 302)
        self.dc.refresh_from_db()
        self.assertEqual(self.dc.desc, 'Test data')