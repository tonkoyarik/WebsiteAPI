import json
from pprint import pprint
from unittest import TestCase

from django.test import Client

from todo.models import Todo


class TodoTestCase(TestCase):
    def test_todo_get(self):
        new_rec = Todo(title='test title',
                       image_url='http://www.halo.com',
                       subtitle='subtitle1',
                       date_time = '2017-12-17 23:50'
                       ).save()

        c = Client()
        response = c.get('/todo/',new_rec)
        pprint(response.data)
        res = response.data['messages'][0]['attachment']['payload']['elements']
        # date_time = res['date_time']
        expected_button = [{'type': 'show_block', 'block_names': ["Datetime"], 'title':'2017-12-17T23:50:00Z'}]
        for i in res:
            self.assertEqual(i['button'],expected_button)

    def test_todo_post(self):
        c = Client()
        record = {'title': 'title1', 'image_url': 'hello', 'subtitle': 'subtitle2', 'date_time':'14/12/17 23:50'}

        response = c.post('/todo/', record)

        pprint(response)


