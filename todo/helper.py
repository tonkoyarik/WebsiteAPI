from rest_framework import serializers

from todo.models import Todo
import json


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('title','image_url','subtitle') #(will return only title and image_url...
        # fields  = '__all__' # will return all fields form models ( Stocck
        # )

