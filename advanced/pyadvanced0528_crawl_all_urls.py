# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:32:05 2022

@author: r-ahmed
"""

####################################################
# Get the target URL page, browse each page
# Download of that page contents
# Extract all desired book links
# Write all book URLs into a file 
####################################################


import re
import requests

def get_url_list():
    print("All URL  function is called")    
    url_lst = []
    for i in range(1, 51):
        url_lst.append(f"https://books.toscrape.com/catalogue/page-{i}.html")
    
    print("Total no of URL is : ", )
    return url_lst
    
def download_url(url):
    print("DL URL function is called")
    dlu = requests.get(url) 
    pgcontent = dlu.text

    return pgcontent

def extract_links(content):
    print("Extract links func is called")
    content = re.sub("\s+", " ", content)
    url_pattern = re.compile('<h3>.*?<a href="(.*?)"')  
    result = re.findall(url_pattern, content)      
    links = []
    for items in result:
        links.append("https://books.toscrape.com/catalogue/" + items + "\n")

    print(len(links))
    return links
   
def save_to_file(filename, links):
    print("File i/o func is called")
    with open(filename, "a") as fp:
#    fp = open(filename, "a")
        # option 1 for writing links in file
        for link in links: # link in List
            fp.write(link)
            fp.write("\n")
        # option 1 for writing links in file
#         fp.writelines(links)

if __name__ == "__main__":
    url = get_url_list()

    for i in range(0,50):
#        print(url[i])   
#    url = "https://books.toscrape.com/catalogue/page-1.html"    # given URL
        content = download_url(url[i])     # keep string contents in content str obj
        links = extract_links(content)  # keep all extracted links in links list obj
#        savetofile(f"bookurls{i}.txt", links)
        save_to_file("bookurls.txt", links)