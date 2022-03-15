# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:40:21 2022

@author: jisra
"""
#variable assignation
galon=3.785411784 #amercian gal in l
mile=1.609344 #american miles in km
cien_km=1/100

def l100kmtompg(liters):
#
# put your code here
    return (galon/(mile*cien_km))/liters 
#

def mpgtol100km(miles):
#
# put your code here
    return (galon/(mile*cien_km))/miles
#

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
