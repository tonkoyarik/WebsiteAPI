from datetime import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from todo.models import Todo, User
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
    reporter = serializers.CharField(allow_null = True,required=False)
    # messenger_id = serializers.CharField(required=False)

    def validate(self, attrs):
        if attrs.get('date_time'):
                try:
                    dt =[datetime.strptime(attrs['date_time'], '%d/%m/%y %H:%M'),
                    datetime.strptime(attrs['date_time'], '%m/%d/%y %H:%M'),
                    datetime.strptime(attrs['date_time'], '%d/%m/%y %I:%M'),
                    datetime.strptime(attrs['date_time'], '%m/%d/%y %I:%M'),
                    datetime.strptime(attrs['date_time'], '%d/%m/%y %I:%M%p')]

                    for i in dt:
                        if i:
                            attrs['date_time'] = i
                            break
                        else:
                            continue
                    return attrs
                except ValueError:
                    raise serializers.ValidationError("Please enter the data in correct format")
        # if attrs.get('messenger user id'):
        #     attrs['messenger_id'] = attrs.get('messenger user id')

#Create validators for Users here:

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name','messenger_id') #(will return only title and image_url...
        # fields  = '__all__' # will return all fields form models ( Stocck
        # )


class UserValidator(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    messenger_id = serializers.CharField()

