from django.db import models
from rest_framework.fields import JSONField


class User(models.Model):
    first_name = models.CharField(max_length=30)
    messenger_id = models.CharField(max_length=30,unique=True)

    def __str__(self):              # __unicode__ on Python 2
        return "%s %s" % (self.first_name, self.last_name)


class Todo(models.Model):
    title = models.CharField(max_length=100,unique=True)  # Like a VARCHAR field
    image_url = models.TextField(blank=False,null=True)  # Like a TEXT field
    subtitle = models.TextField(null=True)
    date_time = models.DateTimeField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(
            self):  # Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name









