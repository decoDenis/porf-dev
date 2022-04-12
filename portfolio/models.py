# from turtle import title
from django.db import models
# from django.forms import CharField, ImageField, URLField
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# indicate wich fields are need for this app 
class project(models.Model):
    title = CharField(max_length=150)
    description = CharField(max_length=500)
    image = ImageField(upload_to="portfolio/images/")
    url = URLField(blank=True)
