from django.db import models

from taggit.managers import TaggableManager

class Resource(models.Model):
    title = models.CharField(max_length=250)
    link = models.URLField()
    description = models.TextField(blank=True)
    for_total_beginners = models.BooleanField(choices=[(True, 'Tak'),(False, 'Nie')])
    tags = TaggableManager()

    def __str__ (self):
        return self.title

    def publish(self):
        self.save()
