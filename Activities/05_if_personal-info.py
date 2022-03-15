# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:36:14 2022

@author: jisra
"""

f_name=input("Ingresa tu primer nombre porfavor: ")
l_name=input("también tu apellido :D: ")
location=input("y tu dirección de entrega: ")
age=input("Por último tu edad: ")
age_n=int(age)
print("\nGracias por tu información.\n")
print("Danos unos momentos mientras verificamos tus datos en nuestro sistema y confirmamos tu orden.")
space=" "
print("\n"*2)
frase="Hola"+space+f_name+space+l_name+space+"confirmamos tu pedido de una pizza hawaiana a la dirección"+space+location+space+"y por tu cumplueaños número"+space+age+space+"hemos añadido un capuchino gratis a tu orden."+ space+"Gracias por preferirnos!"
if age_n<18:
    if age_n<=12:
        print("El cliente es niño y no puede completarse el pedido.")
    else:
        print("El cliente es adolecente.\n")
        print(frase)
elif age_n>=18 and age_n<75:
    print("El cliente es adulto.\n")
    print(frase)
else:
    print("El cliente es adulto mayor.\n")
    print(frase)