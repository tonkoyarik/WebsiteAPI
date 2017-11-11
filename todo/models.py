from django.db import models
from rest_framework.fields import JSONField


class Todo(models.Model):  # Table name, has to wrap models.Model to get the functionality of Django.

    title = models.CharField(max_length=100,unique=True)  # Like a VARCHAR field
    image_url = models.TextField(blank=False,null=True)  # Like a TEXT field
    subtitle = models.TextField(null=True)
    date_time = models.DateTimeField()

    def __unicode__(
            self):  # Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name


''' Create my User table here:
class Users(models.Model):
    name = models.CharField(max_length=20, unique=True)
    messenger_id = models.IntegerField(max_length=100)'''


