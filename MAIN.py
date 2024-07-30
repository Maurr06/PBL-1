import moduloo
import mod2
from random import randint 

print("Hola Mundo!")
lista = [randint(0, 20) for i in range(10)]

print(f"lista = {lista}")

sumatoria = moduloo.suml(lista)
productoria = moduloo.prodl(lista)
cuadratoria = mod2.sqrsl(lista)
paritoria = mod2.divtwol(lista)

print(f"sumatoria = {sumatoria}")
print(f"productoria = {productoria}")
print(f"cuadratoria = {cuadratoria}")
print(f"paritoria = {paritoria}")
print(f"De moduloo, se usaron las funciones {moduloo.__counter} veces")
print(f"De mod2, se usaron las funciones {mod2.__counter2} veces")