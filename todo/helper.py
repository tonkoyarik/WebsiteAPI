from rest_framework import serializers

from todo.models import todo
import json


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = todo
        #fields = ('ticker','volume') (will return only ticker and volume
        fields  = '__all__' # will return all fields form models ( Stocck
        # )

