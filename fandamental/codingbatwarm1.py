# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 01:25:24 2022

@author: r-ahmed
"""

#OK
#def pos_neg(a, b, negative):
#    if a < 0 and b < 0:
#        if negative == True:
#            return True
#        else:
#            return False
#    elif b < 0 or a < 0:
#        if negative == False:
#            return True
#        else:
#            return False
#    else:
#        return False

#print(pos_neg(1, 1, False))

#wrong3
#def pos_neg(a, b, negative):
#    if (a < 0 or b < 0) and negative != True:
#    return True
#  elif (a < 0 and b < 0) and negative == True:
#    return True
#  else:
#    return False

#Wrong 2
#def pos_neg(a, b, negative):
#    if negative == False:
#        if a < 0 or b < 0:
#            return True
#        else:
#            return False
#    elif negative == True:
#        if a < 0 and b < 0:
#            return True
#        else:
#            return False
#    
#print(pos_neg(-1, -1, False))

#1
#def not_string(strg):
#    a = "not"
#    if strg[0:3] != a:
#        strg = a + " " + strg
#        return strg
#    else:
#        strg = strg
#        return strg
#        
#print(not_string("not bad"))


#Given a non-empty string and an int n, return a new string where the char at 
#index n has been removed. The value of n will be a valid index of a char 
#in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#1
#def missing_char(strg, n):
#    for i in range(len(strg)):
#        if i == n:
#            get_str = strg[i]
#            strg = strg.replace(get_str, "")
#    
#    return strg
#    
#print(missing_char("knowledge", 5))
#1W
#def front3(strg):
#    ns = ""
#    
#    if len(strg) < 3:
#        fch = strg[0]
#        lch = strg[1]
#        ns = fch+lch
#    else:
#        fch = strg[0]
#        mch = strg[1]
#        lch = strg[2]
#        ns = fch+mch+lch
#        
#    return ns * 3
    
#print(front3("roman"))
#2 Correct      
#def front3(strg):
#    ns = ""
#    length = len(strg)
#    
#    if length < 3:
#        ns = strg[0:length]
#    else:
#        ns = strg[0:3]
#        
#    return ns * 3
#print(front3("ro"))
    
#def string_bits(strg):
#    li = []
#    for i in range(len(strg)):
#        if strg[i] != strg[i+1]:
#            li.append(i)
#    
#    return str(li)
#
#print(string_bits("heelolo"))


#String Warmup-2

#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'
#what to do?

#1. count the length of the string
#2. for first iteration, return only 1st chr
#3. until last keep increasing chr + 1




#def string_splosion(strg):
#    for i in strg:
#        return i
            
#print(string_splosion("code"))

#def array_count9(nums):
#    s = str(nums)
#    c = 0
#    for i in s:
#        if i == "9":
#            c = c+1
#    return c    
#
#print(array_count9([1,9,2,9,9,9,9,9,1]))
    
#def array_front9(nums):
#    x = 9
#    if x in nums[:3]:
#        return True
#    else:
#        return False

#print(array_front9([1,3,4,4,4,3,9,7,9,6,7]))    

#Not solved by me    
#def check_for_1_3_4(seq):
#    ma = (1,2,3)
#    if ma in zip(seq, seq[1:], seq[2:]):
#        return True
#    else:
#        return False

#print(check_for_1_3_4([1,2,2,3,1,2,3,4,3]))


#def max_end3(nums):
#    if nums[0] > nums[2]:
#        lr = nums[0]
#    else:
#        lr = nums[2]
#    for i in range(len(nums)):
#        nums[i] = lr
#    return nums                
#print(max_end([2,3,5]))


#def sum2(nums):
#    sm = 0
#    if len(nums) == 0:
#        return sm
#    else:
#        if len(nums) < 2:
#            sm = nums[0]
#        else:
#            sm = nums[0]+nums[1]
#    
#    return sm
#print(sum2([1,2]))
    
#def middle_way(a, b):
#    m1 = a[1]
#    m2 = b[1]
#    
#    nl = [m1,m2]
#    return nl
#print(middle_way([2,3,5], [6,8,9]))
    

#def make_ends(nums):
#    i1 = nums[0]
#    i2 = nums[-1]
    
#    nl = [i1, i2]
#    return nl
#print(make_ends([2]))


#def cigar_party(cigars, is_weekend):
#    
#    if (is_weekend != True and (cigars >= 40 and cigars <= 60)) or (is_weekend == True and cigars >= 1):
#        return True
#    else:
#        return False

#print(cigar_party(70, True))

#def date_fashion(you, date):
#    if you <= 2 or date <= 2:
#        return 0
#    elif (you >= 8 and you <= 10) or (date >= 8 and date <= 10):
#        return 2
#    else:
#        return 1
#print(date_fashion(5, 5))
    
#def squirrel_play(temp, is_summer):
#    if (is_summer != True and (temp >= 60 and temp <= 90)) or (is_summer == True and (temp >= 60 and temp <= 100)):
#        return True
#    else:
#        return False
#
#print(squirrel_play(95, True))

#def caught_speeding(speed, is_birthday):
#    if ((speed >= 86 and is_birthday == True) or (is_birthday != True and speed <= 65)):
#        return 0
#    elif ((speed >= 61 and speed <= 85) and is_birthday != True) or (is_birthday == True and (speed >= 65 and speed <= 85)):
#        return 1
#    elif speed >= 86 and is_birthday != True:
#        return 2

#print(caught_speeding(65, True))

#def alarm_clock(day, vacation):
#    if vacation != True and (day >= 1 and day <= 5):
#        return "7:00"
#    elif vacation != True and (day == 0 or day == 6):
#        return "10:00"
#    elif vacation != False and (day >= 1 and day <= 5):
#        return "10:00"
#    elif vacation != False and (day == 0 or day == 6):
#        return "off"
#    
#print(alarm_clock(6,True))

#def in1to10(n, outside_mode):
#    if n >= 1 and n <= 10:
#        if outside_mode != True:
#            return True
#        else:
#            return False
#    elif n >= 10 or n <= 1:
#        if outside_mode != False:
#            return True
#        else:
#            return False

#print(in1to10(10, True))

#OK
#def near_ten(nums):
#    ns = nums[0]
#    nums[0] = nums[1]
#    nums[1] = nums[2]
#    nums[2] = ns
#    return nums

#print(near_ten([2,1,4]))
  
#OK
#def reverse3(nums):
#  ns = nums[0]
#  nums[0] = nums[2]
#  nums[1] = nums[1]
#  nums[2] = ns
#  return nums
    
#print(reverse3([2,4,6]))

#OK
#def string_bits(str):
#    ns = ""
#    for i in range(0, len(str),2):
#        ns = ns + str[i]
#    
#    return ns

#print(string_bits("Hellow"))

#OK
#def string_splosion(strg):
#    ns = ""
#    for i in range(len(strg)+1):
#        for j in range(i):
#            ns = ns + strg[j]
#        
#    return ns
#        
#print(string_splosion("Code"))

#small = 1
#big = 5
#def make_bricks(small, big, goal):

#    given_s_bricks_inch_tot = small * 1
#    given_b_bricks_inch_tot = big * 5
#    
#    total_inch_given = given_s_bricks_inch_tot + given_b_bricks_inch_tot
#    
#    s_bricks_need = goal // s_bricks
#    b_bricks_need = goal // b_bricks
#    
#    inch_calculate = s_bricks_need * 

#print(make_bricks(3, 2, 9))
    

#Almost OK  
#def make_chocolate(small, big, goal):
#    skilo = small * 1
#    bkilo = big * 5
#    
#    tkilo = skilo + bkilo
#    
#    if tkilo < goal:
#        return -1
#    else:
#        if tkilo >= goal:
#            if bkilo == goal:
#                return tkilo - bkilo
#            else:
#                if bkilo != goal:
#                    if skilo == goal or skilo + bkilo >= goal:
#                        return goal - bkilo
#                    
#print(make_chocolate(6, 2, 7))

#OK
#def count_evens(nums):
#    cnt = 0
#    for i in nums:
#        if i % 2 == 0:
#            cnt = cnt + 1
#    return cnt
#
#print(count_evens([2,3,2,4,3,1,4,6,10]))             
            

#def sum13(nums):
#    sm = 0
#    flg = False
#    if 13 in nums:
#        flg = True
#    print(flg)
#    
#    if flg != True:
#        for i in range(len(nums)):
#            sm = sm + nums[i]
#        print("13 not present ", sm)
#    else:
#        ln = len(nums)
#        ind = nums.index(13)
#
#        print("13's index no ", ind)
#        for i in range(0,ind):
#            print("iterate no ", i)
#            print("before sum ", sm)
#            sm = sm + nums[i]
#            print("after sum ", sm)
#        print("13 present ", sm)
#    
#    return sm
        
#half OK
#def sum13(nums):
#    sm = 0
#    flg = False
#    if 13 in nums:
#        flg = True
#    print(flg)
#    
#    if flg != True:
#        for i in range(len(nums)):
#            sm = sm + nums[i]
#        print("13 not present ", sm)
#    else:
#        ind = nums.index(13)
#        print("13's index no ", ind)
#        for i in range(0,ind):
#            print("iterate no ", i)
#            print("before sum ", sm)
#            sm = sm + nums[i]
#            print("after sum ", sm)
#        print("13 present ", sm)
#    
#    return sm
#            
#print(sum13([2,1,1,5,1,13,2]))
        

#OK but!
#def has22(nums):
#    no2 = nums.index(2)
#    
#    if nums[no2+1] == 2:
#        return True
#    else:
#        return False

#print(has22([3,1,3,2,2]))

#OK (google)
#def double(strg):
#    strg1 = ''
#    for char1 in strg:
#        strg1 = strg1 + char1 + char1
#    return strg1

#print(double("The"))
    

#def count_hi(strg):
#    cnt = 0
    
#    if strg.find("hi") != -1:
#        cnt = cnt + 1
    
#    return cnt

#print(count_hi("hi there!"))    


#OK
#def afunct(strg):
#    cnt = 0
#    
#    indx = strg.find("hi")
    
#    for i in range(0, len(strg)):
#        if strg[indx]+strg[indx+1] == "hi":
#            cnt = cnt + 1
#        
#    return cnt
#    
#if __name__ == "__main__":
#    print(afunct("hi'"))

#OK
#def cat_dog(strg):
#    cnt_cat = strg.count("cat")
#    cnt_dog = strg.count("dog")

#    print(cnt_cat, cnt_dog)
#    
#    if cnt_cat == cnt_dog:
#        return True
#    else:
#        return False
#    
#if __name__ == "__main__":
#    print(cat_dog("catdogcat"))


def cat_dog(strg):
    cnt1 = strg.count("code")
    print(cnt1)

    
if __name__ == "__main__":
    print(cat_dog("codedode"))
    






