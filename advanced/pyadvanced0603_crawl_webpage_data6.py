# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:04:48 2022

@author: r-ahmed
"""


###########################################################
# Home work
# Crawl all book details by reding a file
# almost OKOKOKOKOKOKOKOKOK
###########################################################

# 1. read from file
# 2. get individual books url
# 3. get book details(title, price, upc, stock)
# 4. write details into file

import re
import requests

# this is the given main URL. this function is simply returning the main page
def get_url_list():
    url_lst = []
    for i in range(1, 6):
        url_lst.append(f"https://books.toscrape.com/catalogue/page-{i}.html")
    
    return url_lst
    
# get content from the given main URL page
def get_url_content(url):
    url_lists = url
    
    for i in range(0, len(url_lists)):
        url_response = requests.get(url[i])
        content = url_response.text
        content = re.sub('\s+', ' ', content)
        
        book_links = get_book_links(content)
        get_book_url_content(book_links)
#    return 0

# get all book's indivual links in a list
def get_book_links(content):
    content = re.sub("\s+", " ", content)
    url_pattern = re.compile('<h3>.*?<a href="(.*?)"')  
    result = re.findall(url_pattern, content)      
    links = []
    for items in result:
        links.append("https://books.toscrape.com/catalogue/" + items)
    return links

def download_url(url):
    dlu = requests.get(url) 
    pgcontent = dlu.text
    pgcontent = re.sub("\s+", " ", pgcontent)
    return pgcontent

# get individual book page contents
def get_book_url_content(links):
    books_list = links
    print(len(books_list))

    for i in range(0, 20):
        cntnt = download_url(books_list[i])
        book_title = get_book_title(cntnt)
        print(book_title)
        save_to_file("bookdetails5.txt", book_title)
        book_price = get_book_price(cntnt)
        print(book_price)
        save_to_file("bookdetails5.txt", book_price)
        book_upc = get_upc_code(cntnt)
        print(book_upc)
        save_to_file("bookdetails5.txt", book_upc)
        book_stock = get_stock_availability(cntnt)
        print(book_stock)
        save_to_file("bookdetails5.txt", book_stock)
    
    return book_title, book_price,book_upc, book_stock
        
    
def get_book_title(content):
    pattern_for_title = re.compile('<h1>(.*?)<')
    pattern_result = re.findall(pattern_for_title, content)
#    assert len(pattern_result) == 1, "Result must contain at least 1 item!!"
    return pattern_result[0]

def get_book_price(content):
    pattern_for_price = re.compile('<div class=".*?product_main".*?<p class="price_color">(.*?)<')
    pattern_result = re.findall(pattern_for_price, content)
#    assert len(pattern_result) == 1, "Result must contain at least 1 item!!"
    return pattern_result[0]

def get_upc_code(content):
    pattern_for_price = re.compile('<table class=".*?table-striped">.*?<td>(.*?)<')
    pattern_result = re.findall(pattern_for_price, content)
#    assert len(pattern_result) == 1, "Result must contain at least 1 item!!"
    return pattern_result[0]

def get_stock_availability(content):
#    pattern_for_price = re.compile('<table class=".*?table-striped">.*<td>(.*?)<td>')
    pattern_for_price = re.compile('<p class="instock availability">.*?<i class="icon-ok"></i>(.*?)<')
    pattern_result = re.findall(pattern_for_price, content)
#    assert len(pattern_result) == 1, "Result must contain at least 1 item!!"
    return pattern_result[0]

def save_to_file(filename, details):
    with open(filename, "a", encoding="utf-8") as fp:
        fp.write(details)
        fp.write("\n")


if __name__ == "__main__":
    url = get_url_list()
    print(get_url_content(url))
    
    
