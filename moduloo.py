#!/usr/bin/env python3 

""" Modulo.py - Ejemplo de un modulo de Python """

__counter = 0


def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum


def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod


if __name__ == "__main__":
  print("Ejecutando como principal. Haciendo pruebas...")
  from random import randint
  my_list = [randint(1, 100) for i in range(5)]
  print(f"my_list = {my_list}")
  print(f"suml(my_list) = {suml(my_list)}")
  print(f"prodl(my_list) = {prodl(my_list)}")