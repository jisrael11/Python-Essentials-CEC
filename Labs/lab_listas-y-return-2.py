# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:10:47 2022

@author: jisra
"""

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

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end=" ")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
