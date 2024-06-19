import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.name}"
            


class Book(models.Model):
    LANGUAGES = (
        ("AZ", "Az"),
        ("RU", "RU"),
        ("EN", "EN")
    )
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    language = models.CharField(max_length=2, choices=LANGUAGES, null=True, blank=True)
    page_count = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(
        null=True, blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
        )
    
    published_at = models.DateField(null=True, blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


    def __str__(self) -> str:
        return f"{self.name}"
    
    def is_fresh_book(self) -> bool:
        today = datetime.date.today()
        return self.published_at + datetime.timedelta(days=14) >= today
    

    def get_thumbnail_photo_url(self) -> str:
        image_url = self.photos.first()
        return image_url.img.url if image_url else ""
    
    def represent_curency_symbol(self):
        data = {
            "USD": "$"
        }

class BookPhoto(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="photos")
    img = models.ImageField(upload_to="book_photos/%Y/%m/%d")

    class Meta:
        verbose_name = "Book Photo"
        verbose_name_plural = "Book Photos"

    def __str__(self) -> str:
        return f"{self.book.name}"

