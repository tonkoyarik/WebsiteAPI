from rest_framework import serializers

from todo.models import Todo, Users
import json


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('title','image_url','subtitle') #(will return only title and image_url...
        # fields  = '__all__' # will return all fields form models ( Stocck
        # )


class TodoValidator(serializers.Serializer):
    title = serializers.CharField(max_length=100, unique=True)  # Like a VARCHAR field
    image_url = serializers.CharField  # Like a TEXT field
    subtitle = serializers.CharField(null=True)
    button = serializers.DateTimeField()

#Create validators for Users here:
'''
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('name','messenger_id') #(will return only title and image_url...
        # fields  = '__all__' # will return all fields form models ( Stocck
        # )


class UserValidator(serializers.Serializer):
    name = serializers.CharField(max_length=20, unique=True)
    messenger_id = serializers.IntegerField(max_length=100)'''

