#!/usr/bin/env python3 

""" 
Ying.py - Ejemplo de un modulo de Python 
Calcula: Sumatoria, productoria, cuadrados, cubos, euler elevado a n, seno.
"""
from math import sin, e

__counter = 0


def suml(the_list):
  global __counter ; __counter += 1

  the_sum = 0
  for element in the_list:
   the_sum += element

  return the_sum


def prodl(the_list):
  global __counter ; __counter += 1

  prod = 1
  for element in the_list:
   prod *= element
   
  return prod


def cuadrados(the_list):
  global __counter ; __counter += 1
  
  cuads = [element**2 for element in the_list]

  return cuads


def cubos(the_list):
  global __counter ; __counter += 1

  cubos = [element**3 for element in the_list]

  return cubos


def eulerpot(the_list):
  global __counter ; __counter += 1

  eulers = [round(e**element, 2) for element in the_list] 
    
  return eulers


def senos(the_list):
  global __counter ; __counter += 1

  tetas = [round(sin(element), 2) for element in the_list]

  return tetas


def get_counter():
    return __counter



if __name__ == "__main__":
  print("Ejecutando como principal. Haciendo pruebas...")
  from random import randint
  my_list = [randint(1, 100) for i in range(5)]
  print(f"my_list = {my_list}")
  print(f"suml(my_list) = {suml(my_list)}")
  print(f"prodl(my_list) = {prodl(my_list)}")
  print(f"cuadrados(my_list) = {cuadrados(my_list)}")
  print(f"cubos(my_list) = {cubos(my_list)}")
  print(f"eulerpot(my_list) = {eulerpot(my_list)}")
  print(f"senos(my_list) = {senos(my_list)}")
  print(f"__counter = {get_counter()}")