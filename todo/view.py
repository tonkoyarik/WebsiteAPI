import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.helper import StockSerializer
from todo.models import todo
from django.shortcuts import render_to_response
from todo.models import todo


class Todo(APIView):
    def get(self,request):  # Define our function, accept a request

        items = todo.objects.all()  # ORM queries the database for all of the to-do entries.
        serializer = StockSerializer(items, many=True)
        data = serializer.data
        data1 = todo(name=data['title'], description=data['image_url'],created=data['subtitle'])

        for i in data:
            title = i['id']
            image_url = i['name']
            subtitle = i['description']
            buttons = i['created']
            list_goes_here = {"title":title,,,}
        response = {
 "messages": [
    {
      "attachment":{
        "type":"template",
        "payload":{
          "template_type":"list",
          "top_element_style":"large",
          "elements":[
            {
              "title":"Chatfuel Rockets T-Shirt",
              "image_url":"http://rockets.chatfuel.com/img/shirt.png",
              "subtitle":"Soft white cotton t-shirt with CF Rockets logo",
                          },
            {
              "title":"Chatfuel Rockets Hoodie",
              "image_url":"http://rockets.chatfuel.com/img/hoodie.png",
              "subtitle":"Soft gray cotton t-shirt with CF Rockets logo",

            }
          ]
        }
      }
    }
  ]
}
        return Response(response) # Responds with passing the object items (contains info from the DB) to the template index.html

# Create your views here.
