# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:07:39 2022

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

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end=" ")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
