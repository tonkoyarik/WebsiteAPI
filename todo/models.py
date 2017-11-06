from django.db import models


class Todo(models.Model):  # Table name, has to wrap models.Model to get the functionality of Django.

    title = models.CharField(max_length=100, unique=True)  # Like a VARCHAR field
    image_url = models.TextField()  # Like a TEXT field
    subtitle = models.TextField(null=True)
    # Like a DATETIME field

    def __unicode__(
            self):  # Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name
# Create your models here.
