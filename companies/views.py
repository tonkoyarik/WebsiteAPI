from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, request
from .models import Stock
from .serializers import StockSerializer, StockValidator


#LIst all stocks or create a new one
#stocks/
class StockList(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many = True)
        return Response(serializer.data)

    def post(self, request):
        print('*'*50)
        data = request.data
        serializer = StockValidator(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.data
        # print(data['hello'])
        print('*' * 50)
        new_rec = Stock(ticker=validated_data['ticker'], close=validated_data['close'], volume=validated_data['volume'],open=validated_data['open'])
        new_rec.save()
        return Response(request.data)































