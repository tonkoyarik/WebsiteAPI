import json
from pprint import pprint

from django.test import Client, TestCase

from todo import models
from todo.models import Todo, User


class TodoTestCase(TestCase):
    def test_todo_get(self):
        user = User(messenger_id = '874323873872623',
                    first_name='Yarik')
        user.save()
        new_rec = Todo(title='test title',
                       image_url='http://www.halo.com',
                       subtitle='subtitle1',
                       date_time = '2017-12-17 23:50',
                       reporter = user
                       ).save()


        # c = Client()
        response = self.client.get('/todo/', {'messenger user id':'874323873872623'})
        pprint(response.data)
        res = response.data['messages'][0]['attachment']['payload']['elements']
        # date_time = res['date_time']
        expected_button = [{'type': 'show_block', 'block_names': ["Datetime"], 'title':'2017-12-17T23:50:00Z'}]
        for i in res:
            self.assertEqual(i['button'],expected_button)

    def test_todo_post(self):
        user = User(messenger_id='874323873872623',
                    first_name='Yarik')
        user.save()
        record1 = {'title': 'title1', 'image_url': 'hello', 'subtitle': 'subtitle1', 'date_time':'12/12/17 23:50','messenger user id':'874323873872623'}
        response = self.client.post('/todo/', record1)

        pprint(response)

    def test_crete_user(self):
        reporter = {'first name': 'Yarik', 'messenger user id':'28736388287642',}
        responce = self.client.post('/welcome/', reporter)
        user = models.User.objects.get(messenger_id = '28736388287642')
        if user:
            print('Data has been saved')
        else:
            print('Ooops, something went wrong')

        pprint(responce.data)
    def test_todo_get1(self):
        user = User(messenger_id='28736882827648',
                    first_name='Yarik')
        user.save()
        new_rec_1 = Todo(title='test title',
                       image_url='http://www.halo.com',
                       subtitle='subtitle1',
                       date_time='2017-12-17 23:50',
                       reporter=user
                       ).save()
        user2 = User(messenger_id='984976237834',
                    first_name='Nick')
        user2.save()
        new_rec_2 = Todo(title='test title2',
                       image_url='http://www.test2.com',
                       subtitle='subtitle2',
                       date_time='2013-11-17 23:50',
                       reporter=user2
                       ).save()
        response = self.client.get('/todo/',{'messenger user id':'28736882827648'})
        pprint(response.data)
        response = self.client.get('/todo/',{'messenger user id':'984976237834'} )
        pprint(response.data)