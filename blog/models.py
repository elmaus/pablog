from django.db import models
from django.db.models.deletion import PROTECT
from django.utils import timezone

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
)

GENRE_CHOICES = (
    ('blog', 'Blog'),
    ('poetry', "Poetry"),
    ("fiction", "Fiction"),
    ('nonfition', 'Nonfiction')
)

class Book(models.Model):
    category = models.CharField(max_length=20, choices=GENRE_CHOICES, default='Blog')
    title = models.CharField(null=False, max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="media")
    description = models.TextField(default="No descrition", max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.CharField(max_length=20, choices=GENRE_CHOICES, default='Blog')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    title = models.CharField(null=False, max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="media")
    content = models.TextField(null=True)
    excerpt = models.TextField(default="No excert available", max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')

    def __str__(self):
        return self.title

