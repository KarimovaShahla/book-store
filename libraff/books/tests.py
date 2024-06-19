from django.test import TestCase

# Create your tests here.

import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Book


class BookModelTests(TestCase):
    def test_is_fresh_book_with_two_weeks_interval_books(self):
        """
        is_fresh_book() should return True for books whose published_at field is within two weeks, othervise returns False
        """
        today = timezone.now()
        past_time = datetime.date(year=2024, month=5, day=12)

        book = Book(published_at=past_time)
        self.assertFalse(book.is_fresh_book())