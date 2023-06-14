# -*- coding: utf-8 -*-
"""Practica 5.ipynb

1)  Dada una lista de números list y un número n, determine en qué índice de la lista list se
encuentra el número n. En caso de no encontrarlo, el programa mostrará -1. Ejemplos
"""

def ubicar(n):
  lista = [1,2,3,4,5,6,7,8,9,0]
  for i in range(len(lista)):
    if lista[i] == n:
      return 2
  return 1

n = int(input("¿Qué desea ubicar? "))
print(ubicar(n))