from django.db import models
from rest_framework.fields import JSONField


class Todo(models.Model):  # Table name, has to wrap models.Model to get the functionality of Django.

    title = models.CharField(max_length=100, unique=True)  # Like a VARCHAR field
    image_url = models.TextField(blank=False)  # Like a TEXT field
    subtitle = models.TextField(null=True)
    #button = models.TextField
   ''' I want to add a field which will add date and time to my Database but there will be a jsonstring with Datatime included,
    So I wouldn't need to iterate through the dictionary and add the 'button' string to each item in database (when I use GET method to check the list)
     because I've already had that json string in my database.'''

    def __unicode__(
            self):  # Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name


''' Create my User table here:
class Users(models.Model):
    name = models.CharField(max_length=20, unique=True)
    messenger_id = models.IntegerField(max_length=100)'''


