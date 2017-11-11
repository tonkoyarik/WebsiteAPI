from datetime import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from todo.models import Todo
import json


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('title','image_url','subtitle','date_time') #(will return only title and image_url...
        # fields  = '__all__' # will return all fields form models ( Stocck
        # )


class TodoValidator(serializers.Serializer):
    title = serializers.CharField(max_length=100)  # Like a VARCHAR field
    image_url = serializers.CharField(allow_null=True)  # Like a TEXT field
    subtitle = serializers.CharField()
    date_time = serializers.CharField(allow_null=True)

    def validate(self, attrs):
        if attrs.get('date_time'):
            try:
                dt=datetime.strptime(attrs['date_time'], '%d/%m/%y %H:%M')
                attrs['date_time']=dt
                return attrs
            except ValueError:
                raise serializers.ValidationError("Please enter the data in correct format")
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

