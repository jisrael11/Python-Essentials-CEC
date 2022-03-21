# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 21:12:42 2022

@author: jisra
"""

import random

def isYearLeap(year):
#
    """by math def a leap year is exaclty divisible by 4 or 400 
    and it is not divisible by 100"""
    if year%4==0 and (year%100!=0 or year%400==0): 
        return True
    else:
        return False
#

def daysInMonth(year, month):
#
    #defining days for each month except February
    days_month=[31,0,31,30,31,30,31,31,30,31,30,31]
    #if year or month is not integer return None
    if type(year)!=int or type(month)!=int:
        return None
    else:
        if month==2: 
            #if month is February check if year is leap 
            if isYearLeap(year)==True:
                return 29
            else:
                return 28
        else: #if month is not February get days for specific month from list
            return days_month[month-1]  
#

def dayOfYear(year, month, day):
#
    if type(year)!=int or type(month)!=int or type(day)!=int:
        return None
    else:
        #creating a dictionary with month's numbers as keys and month's names as values
        months={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
        return ("Today is {} {}, {}.".format(months[month],day,year)) 
#

print(dayOfYear(2000, 12, 31))
#testing cases
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    result = daysInMonth(yr, mo)
    day = int(random.randrange(1, result))
    print(dayOfYear(yr, mo, day))