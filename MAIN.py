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

def limpiar_todo():
    # Limpiar todas las etiquetas
    lista_label.config(text="Lista: []")
    sumatoria_label.config(text="Sumatoria: ")
    productoria_label.config(text="Productoria: ")
    cuadratoria_label.config(text="Cuadratoria: ")
    cubatoria_label.config(text="Cubatoria: ")
    potencias_label.config(text="Potencias de Euler: ")
    senos_label.config(text="Senos: ")
    rango_label.config(text="Rango: ")
    paritoria_label.config(text="Paritoria: ")
    raicescuad_label.config(text="Raíces Cuadradas: ")
    raicescubs_label.config(text="Raíces Cúbicas: ")
    loges_label.config(text="Logaritmos Naturales: ")
    cosenos_label.config(text="Cosenos: ")

def reiniciar_contadores():
    # Reiniciar contadores de Ying y Yang
    Ying.__counter = 0
    Yang.__counter2 = 0
    messagebox.showinfo("Reiniciar Contadores", "Los contadores se han reiniciado.")

def reiniciar_proceso():
    # Generar nueva lista y ejecutar todas las funciones
    generar_lista()
    calcular_sumatoria()
    calcular_productoria()
    calcular_cuadratoria()
    calcular_cubatoria()
    calcular_potenciaeuler()
    calcular_senos()
    calcular_rango()
    calcular_paritoria()
    calcular_raizcuad()
    calcular_raizcub()
    calcular_logsnats()
    calcular_cos()

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
    potencias_label.config(text=f"Potencias de Euler: {potencias}")

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
    raicescuad_label.config(text=f"Raíces cuadradas: {raicescuad}")

def calcular_raizcub():
    raicescubs = Yang.cub_rad(lista)
    raicescubs_label.config(text=f"Raíces cúbicas: {raicescubs}")

def calcular_logsnats():
    loges = Yang.loge(lista)
    loges_label.config(text=f"Logaritmos naturales: {loges}")

def calcular_cos():
    cosenos = Yang.cosenos(lista)
    cosenos_label.config(text=f"Cosenos: {cosenos}")

# Configuración de la ventana principal
root = tk.Tk()
root.geometry("960x800")
root.title("OPERACIONES")

# Frame superior para la lista y botones de generación
top_frame = tk.Frame(root)
top_frame.pack(pady=20)

tk.Label(top_frame, text="Lista:").pack(side=tk.LEFT, padx=5)
lista_label = tk.Label(top_frame, text="[]")
lista_label.pack(side=tk.LEFT, padx=5)
tk.Button(top_frame, text="Generar Lista", command=generar_lista).pack(side=tk.LEFT, padx=5)

# Frame para los resultados de Ying
ying_frame = tk.LabelFrame(root, text="Operaciones Ying", padx=10, pady=10)
ying_frame.pack(fill="both", expand="yes", padx=20, pady=10)

tk.Button(ying_frame, text="Calcular Sumatoria", command=calcular_sumatoria).grid(row=0, column=0, sticky="ew", pady=5)
sumatoria_label = tk.Label(ying_frame, text="Sumatoria: ")
sumatoria_label.grid(row=0, column=1, sticky="w")

tk.Button(ying_frame, text="Calcular Productoria", command=calcular_productoria).grid(row=1, column=0, sticky="ew", pady=5)
productoria_label = tk.Label(ying_frame, text="Productoria: ")
productoria_label.grid(row=1, column=1, sticky="w")

tk.Button(ying_frame, text="Calcular Cuadratoria", command=calcular_cuadratoria).grid(row=2, column=0, sticky="ew", pady=5)
cuadratoria_label = tk.Label(ying_frame, text="Cuadratoria: ")
cuadratoria_label.grid(row=2, column=1, sticky="w")

tk.Button(ying_frame, text="Calcular Cubatoria", command=calcular_cubatoria).grid(row=3, column=0, sticky="ew", pady=5)
cubatoria_label = tk.Label(ying_frame, text="Cubatoria: ")
cubatoria_label.grid(row=3, column=1, sticky="w")

tk.Button(ying_frame, text="Calcular Potencias de Euler", command=calcular_potenciaeuler).grid(row=4, column=0, sticky="ew", pady=5)
potencias_label = tk.Label(ying_frame, text="Potencias de Euler: ")
potencias_label.grid(row=4, column=1, sticky="w")

tk.Button(ying_frame, text="Calcular Senos", command=calcular_senos).grid(row=5, column=0, sticky="ew", pady=5)
senos_label = tk.Label(ying_frame, text="Senos: ")
senos_label.grid(row=5, column=1, sticky="w")

# Frame para los resultados de Yang
yang_frame = tk.LabelFrame(root, text="Operaciones Yang", padx=10, pady=10)
yang_frame.pack(fill="both", expand="yes", padx=20, pady=10)

tk.Button(yang_frame, text="Calcular Rango", command=calcular_rango).grid(row=0, column=0, sticky="ew", pady=5)
rango_label = tk.Label(yang_frame, text="Rango: ")
rango_label.grid(row=0, column=1, sticky="w")

tk.Button(yang_frame, text="Calcular Paritoria", command=calcular_paritoria).grid(row=1, column=0, sticky="ew", pady=5)
paritoria_label = tk.Label(yang_frame, text="Paritoria: ")
paritoria_label.grid(row=1, column=1, sticky="w")

tk.Button(yang_frame, text="Calcular Raíces Cuadradas", command=calcular_raizcuad).grid(row=2, column=0, sticky="ew", pady=5)
raicescuad_label = tk.Label(yang_frame, text="Raíces Cuadradas: ")
raicescuad_label.grid(row=2, column=1, sticky="w")

tk.Button(yang_frame, text="Calcular Raíces Cúbicas", command=calcular_raizcub).grid(row=3, column=0, sticky="ew", pady=5)
raicescubs_label = tk.Label(yang_frame, text="Raíces Cúbicas: ")
raicescubs_label.grid(row=3, column=1, sticky="w")

tk.Button(yang_frame, text="Calcular Logaritmos Naturales", command=calcular_logsnats).grid(row=4, column=0, sticky="ew", pady=5)
loges_label = tk.Label(yang_frame, text="Logaritmos Naturales: ")
loges_label.grid(row=4, column=1, sticky="w")

tk.Button(yang_frame, text="Calcular Cosenos", command=calcular_cos).grid(row=5, column=0, sticky="ew", pady=5)
cosenos_label = tk.Label(yang_frame, text="Cosenos: ")
cosenos_label.grid(row=5, column=1, sticky="w")


# Crear un Frame para los botones finales
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=20)

# Botones final
tk.Button(bottom_frame, text="Mostrar Contadores", command=mostrar_contadores).pack(side=tk.LEFT, padx=10)
tk.Button(bottom_frame, text="Limpiar", command=limpiar_todo).pack(side=tk.LEFT, padx=10)
tk.Button(bottom_frame, text="Reiniciar Contadores", command=reiniciar_contadores).pack(side=tk.LEFT, padx=10)
tk.Button(bottom_frame, text="Nuevo", command=reiniciar_proceso).pack(side=tk.LEFT, padx=10)

# Ejecutar el loop principal de Tkinter
root.mainloop()
