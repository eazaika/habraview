#!/usr/bin/env python3
import json
from habradata import view

class Data:
    HABR = 'habr.json'

    def __init__(self):
        try:
            with open(self.HABR, 'r', encoding='utf-8'):
                pass
        except FileNotFoundError:
            with open(self.HABR, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def get_data(self):
        with open(self.HABR, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            return data

    def html_list_json(self):
        with open(self.HABR, 'r', encoding='utf-8') as f:
            habr = json.load(f)
        posts = []
        for post in habr:
            content = post['author'] + ' __ ' + post['stars'] + ' : ' + post['title']
            posts.append(content)
        return '<br>'.join(posts)

    def html_list_db(self):
        posts = []
        for post in view.data(self):
            content = post['author'] + ' __ ' + post['stars'] + ' : ' + post['title']
            posts.append(content)
        return '<br>'.join(posts)
