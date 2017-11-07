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
                       ).save()

        c = Client()
        response = c.get('/todo/',new_rec)
        pprint(response.data)
        res = response.data['messages'][0]['attachment']['payload']['elements']
        expected_button = [{'title': 'View Item', 'type': 'web_url', 'url': 'https://rockets.chatfuel.com/store/shirt'}]
        for i in res:
            self.assertEqual(i['button'],expected_button)
