from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from comicsdb.models import Creator
from comicsdb.serializers import CreatorSerializer
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


class GetAllCreatorsTest(TestCaseBase):

    @classmethod
    def setUpTestData(cls):
        cls._create_user(cls)

        Creator.objects.create(name='John Byrne', slug='john-byrne')
        Creator.objects.create(name='Walter Simonson', slug='walter-simonson')

    def setUp(self):
        self._client_login()

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('api:creator-list'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_unauthorized_view_url(self):
        self.client.logout()
        resp = self.client.get(reverse('api:creator-list'))
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)


class GetSingleCreatorTest(TestCaseBase):

    @classmethod
    def setUpTestData(cls):
        cls._create_user(cls)

        cls.jack = Creator.objects.create(name='Jack Kirby', slug='jack-kirby')
        Creator.objects.create(name='Steve Ditko', slug='steve-ditko')

    def setUp(self):
        self._client_login()

    def test_get_valid_single_creator(self):
        response = self.client.get(reverse('api:creator-detail',
                                           kwargs={'pk': self.jack.pk}))
        creator = Creator.objects.get(pk=self.jack.pk)
        serializer = CreatorSerializer(creator)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_creator(self):
        response = self.client.get(reverse('api:creator-detail',
                                           kwargs={'pk': '10'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthorized_view_url(self):
        self.client.logout()
        response = self.client.get(reverse('api:creator-detail',
                                           kwargs={'pk': self.jack.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)