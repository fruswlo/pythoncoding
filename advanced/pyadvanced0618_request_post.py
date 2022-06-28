# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 23:39:28 2022

@author: r-ahmed
"""

import requests


def post_request():
    rspns = requests.post('https://httpbin.org/post', data={'custname': 'ANAME','custemail':'ANEMAIL@email.com','custtel':'12345','delivery':'15:00','size':'small','topping':'onion,cheese','comments':'ASAP'})
    post_response_result = rspns.text
    return post_response_result
#    print(post_response_result)


def put_request():
    rspns = requests.put("https://httpbin.org/put", data={"name":"roman", "class":"pyadv", "start":"2022-05","end":"2022-08"})
    put_response_result = rspns.text
    return put_response_result
#    print(put_response_result)

#Difference between PUT and POST methods
#Generally, in practice, always use PUT for UPDATE operations.
#Always use POST for CREATE operations.

def head_request():
    rspns = requests.head('https://books.toscrape.com/catalogue/page-1.html')
    hed_response_result = rspns.headers
    return hed_response_result
#    print(hed_response_result)

if __name__ == "__main__":
    print(post_request())
    print(put_request())
    print(head_request())