import json
from django.db import connections, connection
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from todo import models
from todo.helper import StockSerializer, TodoValidator, UserValidator, UserSerializer
from django.shortcuts import render_to_response
from todo.models import Todo, User


class Delete(APIView):
    def post(self, request):
        data = request.data
        u_id = data['messenger user id']
        title1 = data['title']

        with connection.cursor() as c:
            c.execute('''DELETE FROM todo_todo WHERE title =%s AND reporter_id = %s''',(title1,u_id))
            c.fetchone()
        data1 = Todo.objects.all()
        serializer = StockSerializer(data1, many=True)
        return Response(serializer.data)




class Welcome(APIView):
    def post(self,request):
        r = request.data
        new_record = User(first_name = r['first name'],messenger_id = r['messenger user id'])
        new_record.save()
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data)


class TodoView(APIView):
    def get(self, request):  # Define our function, accept a request

        data = request.GET
        u_id = data['messenger user id']
        user = models.User.objects.get(messenger_id=u_id)

        stocks = Todo.objects.filter(reporter=user)
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
        print(data)

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
        print(validated_data)
        # print(data['hello'])
        print('*' * 50)
        u_id = data['messenger user id']
        user = models.User.objects.get(messenger_id=u_id)
        new_rec = Todo(title=validated_data['title'], image_url=validated_data['image_url'],
                       subtitle=validated_data['subtitle'],date_time=validated_data['date_time'],reporter = user)
        new_rec.save()
        return Response(serializer.data)

    # Responds with passing the object items (contains info from the DB) to the template index.html

    # Create your views here.
