# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:09:57 2022

@author: jisra
"""

file=open("devices.txt","a")
while True:
    newItem=input("Enter new device name: ")
    if newItem=="exit":
        print("All done!")
        break
    file.write(newItem+"\n")
file.close()