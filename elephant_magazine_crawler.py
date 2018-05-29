#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

#article id, 1071 when written
RANGE = 1100

for i in range(RANGE):
    try:
        URL = "http://app.idaxiang.org/api/v1_0/art/info?id={}".format(i)
        response = requests.get(URL)        
        title = response.json()['body']['article']['title']
        title = "{}. {}".format(i, title)
        #article body of html without header
        body = response.json()['body']['article']['content']
        #every article is a html file
        with open("{}.html".format(title), 'a') as article:
            #article.css for style later
            article.write('<!DOCTYPE html><html> <head> <link rel="stylesheet" href="article.css"> </head> <body>')
            article.write(body)
            article.write('</body> </html>')
        #article table for quick reference
        with open('root.html', 'a') as table:
            table.write('<!DOCTYPE html><html> <head> <link rel="stylesheet" href="table.css"> </head> <body>')
            #replace with space with '%20' in a href
            table.write('<a target="_blank" href={}.html>{}</a>'.format(title.replace(' ', '%20'), title))
            table.write('<br />')
            table.write('</body> </html>')            
        print(title)
    except:
        continue