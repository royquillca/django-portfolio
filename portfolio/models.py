from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = CharField(max_length=150)
    description = CharField(max_length=150)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)