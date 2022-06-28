# -*- coding: utf-8 -*-
"""
Created on Sun May 29 19:31:05 2022

@author: r-ahmed
"""

#from itertools import groupby
import re

webtext = """
<p>As always, please feel free <a href="/contact/">to get in touch with us here at Intoli</a>.
Our team has broad expertise in web scraping and data intelligence, and we would really love to hear about what you&rsquo;re working on.
We also have <a href="http://intoli.us11.list-manage.com/subscribe?u=e95178aac513dc319bf87a9c3&amp;id=bb722b0e5d">a pretty awesome monthly newsletter</a> where we send out our favorite articles every month!</p>

"""


# we need to extract href link from the above text
# Soluton 1, using string algorithm

split_main_string = webtext.split()

# Try 1
#get_string = [st for st in split_main_string if "href" in st]
#print(get_string)
#new_string = str(get_string)[:str(get_string).rfind("?")]
#indx = new_string.index("http")    
#print(new_string[indx:])
#url_string = new_string[31:]
#print(url_string)

#OK
split_sub_string = str(split_main_string).split('">a')
#print(split_sub_string)
#print()
get_url_st = split_sub_string[0]
#print(get_url_st)
#print()
indx = get_url_st.index("http")    
print(get_url_st[indx:])
print()

#Option 2 using magic method of string class
#str_match = [s for s in my_list if s.__contains__("ack")]
#print(str_match)

#for k, g in groupby(enumerate(webtext), lambda x: not x[1].isspace()):
#    if k:
#        pos, first_item = next(g)
#        print(pos, first_item + ''.join([x for _, x in g]))
#    
#print(webtext[249:348])


# Solution 2 using RE (regular expression)

# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto    #recommened

text = """
Person1, 01712066727, Person2, 01819494585, Person3, 01511234543 01211098234
"""

#url_pattern1 = re.compile('<a href="(ht.*?)"')
#url_pattern2 = re.compile('(\d*)')
#url_pattern3 = re.compile('(\d+)')
#url_pattern4 = re.compile('(\d{11})')
url_pattern5 = re.compile('(01[785]\d{8})')
# we are creating a pattern to extract such string, which matches a href and
# then full string until "?" quation mark 

# explanation of above url pattern1: within the parenthesis (), when python will
# find next " along with ? question mark. if we do not put the ? mark, then it
# will find the next until ". So, if we put ? mark then python re will stop as
# soon as it finds first " inverted 

# explanation of above url pattern2: \d returns all digits. and a * returns 
# all no inluding spaces
# explanation of above url pattern3: \d returns all digits. and a + returns 
# all numbers only omitting spaces
# explanation of url pattern4 : {11} means, when we want to resutn only digits
# of all 11 digits
# explanation of url pattern5 : 01 means, it will cchek all digits with 01, then
# [785] means, those numbers start with 7 or 8, 5 followed by 01, and later 
# as above \d meand rest 8 digits 

#result = re.findall(url_pattern1, webtext)
result = re.findall(url_pattern5, text)
# what we did here is, since we have created a pattern to get url, so taking a 
# variable result, to keep the extracted url as per pattern from the given str

print(result)

text2 = """
   Person1, 01712066727     , Person2,      01819494585,      Person3,      01511234543      01211098234
"""

print(text2)
text2 = text2.strip()
text3 = re.sub("\s", "", text2)
text4 = re.sub("\s+", " ", text2)
text5 = re.sub("\s+", " ", text2)
# this strip() is a string calss builtin method. called via text2 object. which
# is a string class object. acting here as a str variable

# explanation of pattern text3: calling a method name sub() [substitute] from 
# re calss, which has a default pattern.\s means, all whitespace will be "" means
# replaced by ""=empty and last args is which string is passing

# explanation of pattern text4: when there are multiple whitespace then \s+ is
# is used, and " " replaced by 1 space




# a stript() method is used to remove all front and rear whitespaces from a str

print(text2)
print(text3)
print(text4)