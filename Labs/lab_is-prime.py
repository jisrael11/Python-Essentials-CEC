# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:14:59 2022

@author: jisra
"""

def isPrime(num):
#
# Su codigo Aqui
    if num>1: #checking if the # is greater than 1
        if num==2: #2 is a prime number 
            return True
        else:
            for i in range(2,num): #for loop to go from 2 to the tested number
                if num%i==0: #is divisible for the # i
                    return False #if numb has a exact division for i!=num is not prime
            return True #if num is only divisible for itself is prime
    else: #if num <= 1 is not prime
        return False
#

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
