#!/usr/bin/env python3 

""" 
Yang.py - ejemplo de otro modulo en Python. 
Calcula: diferencia de mayor con menor, division por dos, raiz cuadrada, raiz cubica, logaritmos naturales, coseno. 
"""
from math import cos, log, e
__counter2 = 0



def rango(the_list):
  global __counter2 ; __counter2 += 1

  lista = sorted(the_list)
  diff = lista[len(lista)-1] - lista[0]

  return diff


def divtwol(the_list):
  global __counter2 ; __counter2 += 1

  divs = [element/2 for element in the_list] 
  
  for i in range(len(divs)): # Convierte los "n.0" a "n"
    if divs[i] - int(divs[i]) == 0:
      divs[i] = int(divs[i])

  return divs


def cuad_rad(the_list):
  global __counter2 ; __counter2 += 1
  
  raices = [round(element**(1/2), 2) for element in the_list]

  return raices


def cub_rad(the_list):
  global __counter2 ; __counter2 += 1
  
  raices = [round(element**(1/3), 2) for element in the_list]

  return raices


def loge(the_list):
  global __counter2 ; __counter2 += 1
  
  try:
    loges = [round(log(element, e), 2) for element in the_list]

  except ValueError:
    loges = []

    for element in the_list:
      if element <= 0: 
        loges.append("N/A")
      else: 
        loges.append(round(log(element, e), 2))
        
  return loges


def cosenos(the_list):
  global __counter2 ; __counter2 += 1
  
  cotetas = [round(cos(element), 2) for element in the_list]

  return cotetas


def get_counter2():
    return __counter2


if __name__ == "__main__":
  print("Ejecutando como principal. Haciendo pruebas...")
  from random import randint
  my_list = [randint(1, 100) for i in range(5)]
  print(f"my_list = {my_list}")

  print(f"rango(the_list) = {rango(my_list)}") 
  print(f"divtwol(my_list) = {divtwol(my_list)}")
  print(f"cuad_rad(the_list) = {cuad_rad(my_list)}") 
  print(f"cub_rad(my_list) = {cub_rad(my_list)}")
  print(f"loge(the_list) = {loge(my_list)}") 
  print(f"cosenos(my_list) = {cosenos(my_list)}")
  print(f"__counter2 = {__counter2}")