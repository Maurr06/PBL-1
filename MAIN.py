#!/usr/bin/env python3 

import Ying
import Yang

from random import randint
import tkinter as tk
from tkinter import messagebox

# Definir las funciones del GUI
def generar_lista():
    global lista
    lista = [randint(0, 20) for i in range(10)]
    lista_label.config(text=f"Lista: {lista}")

def calcular_sumatoria():
    sumatoria = Ying.suml(lista)
    sumatoria_label.config(text=f"Sumatoria: {sumatoria}")

def calcular_productoria():
    productoria = Ying.prodl(lista)
    productoria_label.config(text=f"Productoria: {productoria}")

def calcular_cuadratoria():
    cuadratoria = Ying.cuadrados(lista)
    cuadratoria_label.config(text=f"Cuadratoria: {cuadratoria}")

def calcular_paritoria():
    paritoria = Yang.divtwol(lista)
    paritoria_label.config(text=f"Paritoria: {paritoria}")

def mostrar_contadores():
    contadores = f"De moduloo, se usaron las funciones {Ying.get_counter()} veces\n" \
                 f"De mod2, se usaron las funciones {Yang.get_counter2()} veces"
    tk.messagebox.showinfo("Contadores", contadores)

# Configuración de la ventana principal
root = tk.Tk()
root.geometry("960x600")  # Tamaño inicial de la ventana
root.title("Programa de Ejemplo")

lista_label = tk.Label(root, text="Lista: []")
lista_label.pack(pady=10)

sumatoria_label = tk.Label(root, text="Sumatoria: ")
sumatoria_label.pack()

productoria_label = tk.Label(root, text="Productoria: ")
productoria_label.pack()

cuadratoria_label = tk.Label(root, text="Cuadratoria: ")
cuadratoria_label.pack()

paritoria_label = tk.Label(root, text="Paritoria: ")
paritoria_label.pack()

tk.Button(root, text="Generar Lista", command=generar_lista).pack(pady=20)
tk.Button(root, text="Calcular Sumatoria", command=calcular_sumatoria).pack()
tk.Button(root, text="Calcular Productoria", command=calcular_productoria).pack()
tk.Button(root, text="Calcular Cuadratoria", command=calcular_cuadratoria).pack()
tk.Button(root, text="Calcular Paritoria", command=calcular_paritoria).pack()
tk.Button(root, text="Mostrar Contadores", command=mostrar_contadores).pack()

# Ejecutar el loop principal de Tkinter
root.mainloop()
