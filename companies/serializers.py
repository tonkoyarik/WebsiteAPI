from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        #fields = ('ticker','volume') (will return only ticker and volume
        fields  = '__all__' # will return all fields form models ( Stocck)


class StockValidator(serializers.Serializer):
    ticker = serializers.CharField(max_length=10)
    open = serializers.FloatField()
    close = serializers.FloatField()
    volume = serializers.IntegerField()