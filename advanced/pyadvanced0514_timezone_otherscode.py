# -*- coding: utf-8 -*-
"""
Created on Mon May 23 01:26:06 2022

@author: r-ahmed
"""

def show_local_time():
    from datetime import datetime
    import pytz
    
    print("PLease enter your desired City name for Timezone")
    city_name = input()
    city_name = city_name.lower()
    
    if city_name == "dhaka":
        tz_dhk = pytz.timezone("Asia/Dhaka")
        dt_dhk = datetime.now(tz_dhk)
        return tz_dhk
        return dt_dhk
    elif city_name == "tokyo":
        tz_tok = pytz.timezone("Asia/Tokyo")
        dt_tok = datetime.now(tz_tok)
        return tz_tok
        return dt_tok
    elif city_name == "london":
        tz_ldn = pytz.timezone("Europe/London")
        dt_ldn = datetime.now(tz_ldn)
        return tz_ldn
        return dt_ldn
    elif city_name == "newyork":
        tz_nyc = pytz.timezone("America/NewYork")
        dt_nyc = datetime.now(tz_nyc)
        return tz_nyc
        return dt_nyc
    else:
        print("Timezone Unavailable!!!")
        
print(show_local_time())
    