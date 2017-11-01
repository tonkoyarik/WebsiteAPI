from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.models import todo
from django.shortcuts import render_to_response
from todo.models import todo

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = todo
        #fields = ('ticker','volume') (will return only ticker and volume
        fields  = '__all__' # will return all fields form models ( Stocck
        # )
class Todo(APIView):
    def get(self,request):  # Define our function, accept a request

        items = todo.objects.all()  # ORM queries the database for all of the to-do entries.
        serializer = StockSerializer(items, many=True)
        return Response(serializer.data) # Responds with passing the object items (contains info from the DB) to the template index.html

# Create your views here.
