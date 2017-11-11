import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.helper import StockSerializer, TodoValidator
from django.shortcuts import render_to_response
from todo.models import Todo


class TodoView(APIView):
    def get(self, request):  # Define our function, accept a request

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
        stocks = Todo.objects.all()
        serializer = StockSerializer(stocks, many=True)
        list_goes_here = serializer.data

        for i in list_goes_here:
            date_time = i['date_time']
            i['button'] = [
                {
              "type": "show_block",
              "block_names": ["Datetime"],
              "title": date_time
            }
            ]
            del i['date_time']
        response = {
            "messages": [
                {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "list",
                            "top_element_style": "large",
                            "elements": list_goes_here
                        }
                    }
                }
            ]
        }
        return Response(response)



    def post(self, request):
        print('*' * 50)
        data = request.data
        serializer = TodoValidator(data=data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as r:
            print(r)
            return JsonResponse({
                "messages": [
                    {"text": "I need you to enter Title, Description and DataTime in format (dd/mm/yy 23:50)"},
                ]
            })

        validated_data = serializer.data
        # print(data['hello'])
        print('*' * 50)
        new_rec = Todo(title=validated_data['title'], image_url=validated_data['image_url'],
                       subtitle=validated_data['subtitle'],date_time=validated_data['date_time'])
        new_rec.save()
        return Response(serializer.data)

    # Responds with passing the object items (contains info from the DB) to the template index.html

    # Create your views here.
