#!/usr/bin/env python3 

""" mod2.py - ejemplo de otro modulo en Python """

__counter2 = 0


def sqrsl(the_list):
  global __counter2
  __counter2 += 1
  
  sqrs = []
  for element in the_list:
    sqrs.append(element**2)

  return sqrs


def divtwol(the_list):
  global __counter2
  __counter2 += 1

  divs = []
  for element in the_list:
   divs.append(element/2)

  return divs


if __name__ == "__main__":
  print("Ejecutando como principal. Haciendo pruebas...")
  from random import randint
  my_list = [randint(1, 100) for i in range(5)]
  print(f"my_list = {my_list}")
  print(f"sqrsl(my_list) = {sqrsl(my_list)}")
  print(f"divtwol(my_list) = {divtwol(my_list)}")