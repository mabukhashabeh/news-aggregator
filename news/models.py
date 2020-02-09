from django.db import models
from django.conf import Settings

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    url = models.TextField(null=True)
    date = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)

    def __str__(self):
        return self.title