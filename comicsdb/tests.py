import datetime

from django.test import TestCase
from django.utils.text import slugify

from comicsdb.models import Publisher, Series, SeriesType


class PublisherTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        found_date = datetime.date(1934, 1, 1)
        cls.name = 'DC Comics'
        cls.slug = slugify(cls.name)
        cls.short_desc = 'Home of Superman'

        cls.publisher = Publisher.objects.create(name=cls.name, slug=cls.slug,
                                                 short_desc=cls.short_desc, founded=found_date)

        on_going_series = SeriesType.objects.create(name='Ongoing Series')

        Series.objects.create(name='Superman', slug='superman', sort_name='Superman',
                              type=on_going_series, publisher=cls.publisher, volume=1,
                              year_began=1939, short_desc='The one that started it all.')

    def test_series_count(self):
        self.assertEqual(self.publisher.series_count, 1)

    def test_publisher_creation(self):
        self.assertTrue(isinstance(self.publisher, Publisher))
        self.assertEqual(str(self.publisher), self.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.publisher._meta.verbose_name_plural),
                         "publishers")


class SeriesTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        publisher = Publisher.objects.create(
            name='DC Comics', slug='dc-comics')
        series_type = SeriesType.objects.create(name='Ongoing Series')
        cls.name = 'Superman'
        cls.superman = Series.objects.create(name=cls.name, slug=slugify(cls.name),
                                             sort_name=cls.name, type=series_type,
                                             publisher=publisher, year_began=1939)

    def test_series_creation(self):
        self.assertTrue(isinstance(self.superman, Series))
        self.assertEqual(str(self.superman), self.name)

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(self.superman._meta.verbose_name_plural), 'Series')


class SeriesTypeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.name = 'Mini-Series'
        cls.notes = 'A short series typically four issues'

        cls.series_type = SeriesType.objects.create(name=cls.name,
                                                    notes=cls.notes)

    def test_seriestype_creation(self):
        self.assertTrue(isinstance(self.series_type, SeriesType))
        self.assertEqual(str(self.series_type), self.name)