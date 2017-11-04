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

        # items = tod.objects.all()  # ORM queries the database for all of the to-do entries.
        # serializer = StockSerializer(items, many=True)
        # data = serializer.data
        # data1 = tod(name=data['title'], description=data['image_url'],created=data['subtitle'])
        #
        # for i in data:
        #     title = i['id']
        #     image_url = i['name']
        #     subtitle = i['description']
        #     buttons = i['created']
        #     list_goes_here = {"title":title,,,}
        stocks = todo.objects.all()
        serializer = StockSerializer(stocks, many=True)
        list_goes_here = serializer.data
        ''' I have to change name, description and created in models.py!!!' 
        Serializer.data have to responce the data as presented in responce1 
        and responce2( the same keys should be presented in Responce)'''

        responce1= {
                                "title": "First todo task",
                                "image_url": "https://rockets.chatfuel.com/store/shirt",
                                "subtitle": "I will create a new item in the Todo table in my database",
                                "buttons":[
                {
                  "type":"web_url",
                  "url":"https://rockets.chatfuel.com/store/shirt",
                  "title":"View Item"
                }
              ],
                            }
        responce2 = {
                                "title": "Second todo task",
                                "image_url": "https://rockets.chatfuel.com/store/shirt",
                                "subtitle": "Here is my second todo task",
                                "buttons":[
                {
                  "type":"web_url",
                  "url":"https://rockets.chatfuel.com/store/shirt",
                  "title":"View Item"
                }
              ],
                            }

        response = {
 "messages": [
    {
      "attachment":{
        "type":"template",
        "payload":{
          "template_type":"list",
          "top_element_style":"large",
          "elements":[
              responce1,responce2,
          ]
        }
      }
    }
  ]
}
        return Response(response) # Responds with passing the object items (contains info from the DB) to the template index.html

# Create your views here.
