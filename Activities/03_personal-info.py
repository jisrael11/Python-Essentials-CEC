# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:37:20 2022

@author: jisra
"""

f_name=input("Ingresa tu primer nombre porfavor: ")
l_name=input("también tu apellido :D: ")
location=input("y tu dirección de entrega: ")
age=input("Por último tu edad: ")
print("\nGracias por tu información.\n")
print("Danos unos momentos mientras verificamos tus datos en nuestro sistema y confirmamos tu orden.")
space=" "
print("\n"*2)
print("Hola"+space+
      f_name+space+
      l_name+space+
      "confirmamos tu pedido de una pizza hawaiana a la dirección"+space+
      location+space+"y por tu cumplueaños número"+space+
      age+space+"hemos añadido un capuchino gratis a tu orden."+ 
      space+"Gracias por preferirnos!")