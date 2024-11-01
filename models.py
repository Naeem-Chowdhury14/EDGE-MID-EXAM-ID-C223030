from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_publication_year(value):
    current_year = timezone.now().year
    if value > current_year:
        raise ValidationError("The publication year cannot be in the future.")

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField(validators=[validate_publication_year])

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"