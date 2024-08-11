#!/usr/bin/env python3 

import Ying
import Yang

from random import randint
import tkinter as tk
from tkinter import messagebox

# 
# Definir las funciones del GUI 
# 

def generar_lista():
    global lista
    lista = [randint(0, 20) for i in range(10)]
    lista_label.config(text=f"Lista: {lista}")

def mostrar_contadores():
    contadores = f"De {Ying.__name__}, se usaron las funciones {Ying.get_counter()} veces\n" \
                 f"De {Yang.__name__}, se usaron las funciones {Yang.get_counter2()} veces"
    tk.messagebox.showinfo("Contadores", contadores)


# Ying
def calcular_sumatoria():
    sumatoria = Ying.suml(lista)
    sumatoria_label.config(text=f"Sumatoria: {sumatoria}")

def calcular_productoria():
    productoria = Ying.prodl(lista)
    productoria_label.config(text=f"Productoria: {productoria}")

def calcular_cuadratoria():
    cuadratoria = Ying.cuadrados(lista)
    cuadratoria_label.config(text=f"Cuadratoria: {cuadratoria}")

def calcular_cubatoria():
    cubatoria = Ying.cubos(lista)
    cubatoria_label.config(text=f"Cubatoria: {cubatoria}")

def calcular_potenciaeuler():
    potencias = Ying.eulerpot(lista)
    potencias_label.config(text=f"Potencias de euler: {potencias}")

def calcular_senos():
    senos = Ying.senos(lista)
    senos_label.config(text=f"Senos: {senos}")



# Yang
def calcular_rango():
    rango = Yang.rango(lista)
    rango_label.config(text=f"Rango: {rango}")

def calcular_paritoria():
    paritoria = Yang.divtwol(lista)
    paritoria_label.config(text=f"Paritoria: {paritoria}")

def calcular_raizcuad():
    raicescuad = Yang.cuad_rad(lista)
    raicescuad_label.config(text=f"Raices cuadradas: {raicescuad}")

def calcular_raizcub():
    raicescubs = Yang.cub_rad(lista)
    raicescubs_label.config(text=f"Raices cubicas: {raicescubs}")

def calcular_logsnats():
    loges = Yang.loge(lista)
    loges_label.config(text=f"Logaritmos naturales: {loges}")

def calcular_cos():
    cosenos = Yang.cosenos(lista)
    cosenos_label.config(text=f"Cosenos: {cosenos}")

#
# Configuración de la ventana principal
#

root = tk.Tk()
root.geometry("960x600")
root.title("Programa de Ejemplo")

# Presentar resultados
# YING
lista_label = tk.Label(root, text="Lista: []")
lista_label.pack(pady=10)

sumatoria_label = tk.Label(root, text="Sumatoria: ")
sumatoria_label.pack()

productoria_label = tk.Label(root, text="Productoria: ")
productoria_label.pack()

cuadratoria_label = tk.Label(root, text="Cuadrados: ")
cuadratoria_label.pack()

cubatoria_label = tk.Label(root, text="Cubos: ")
cubatoria_label.pack()

potencias_label = tk.Label(root, text="Potencias de euler: ")
potencias_label.pack()

senos_label = tk.Label(root, text="Senos: ")
senos_label.pack()

# YANG
rango_label = tk.Label(root, text="Rango: ")
rango_label.pack()

paritoria_label = tk.Label(root, text="Paritoria: ")
paritoria_label.pack()

raicescuad_label = tk.Label(root, text="Raices cuadradas: ")
raicescuad_label.pack()

raicescubs_label = tk.Label(root, text="Raices cubicas: ")
raicescubs_label.pack()

loges_label = tk.Label(root, text="Logaritmos Naturales: ")
loges_label.pack()

cosenos_label = tk.Label(root, text="Cosenos: ")
cosenos_label.pack()

# CREACION DE BOTONES #
tk.Button(root, text="Generar Lista", command=generar_lista).pack(pady=20)
tk.Button(root, text="Calcular Sumatoria", command=calcular_sumatoria).pack()
tk.Button(root, text="Calcular Productoria", command=calcular_productoria).pack()
tk.Button(root, text="Calcular Cuadratoria", command=calcular_cuadratoria).pack()
tk.Button(root, text="Calcular Cubatoria", command=calcular_cubatoria).pack()
tk.Button(root, text="Calcular Potencias de euler", command=calcular_potenciaeuler).pack()
tk.Button(root, text="Calcular senos", command=calcular_senos).pack()

tk.Button(root, text="Calcular Rango", command=calcular_rango).pack(pady=20)
tk.Button(root, text="Calcular Paritoria", command=calcular_paritoria).pack()
tk.Button(root, text="Calcular Raices cuadradas", command=calcular_raizcuad).pack()
tk.Button(root, text="Calcular Raices cubicas", command=calcular_raizcub).pack()
tk.Button(root, text="Calcular Logaritmos naturales", command=calcular_logsnats).pack()
tk.Button(root, text="Calcular Cosenos", command=calcular_cos).pack()

tk.Button(root, text="Mostrar Contadores", command=mostrar_contadores).pack()

# Ejecutar el loop principal de Tkinter
root.mainloop()
