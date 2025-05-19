import tkinter as tk
import csv
import os
from datetime import datetime

ARCHIVO = "data/gastos.csv"
os.makedirs("data", exist_ok=True)

ventana = tk.Tk()
ventana.title("Gestor de Gastos")
ventana.geometry("400x400")  # Un poco más alto para ver la lista

def guardar_gasto_csv(monto, categoria):
    with open(ARCHIVO, mode="a", newline="") as archivo:
        campos = ["monto", "categoria", "fecha"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if archivo.tell() == 0:
            escritor.writeheader()
        escritor.writerow({
            "monto": monto,
            "categoria": categoria,
            "fecha": datetime.today().strftime("%Y-%m-%d")
        })

def agregar_gasto():
    monto = entrada_monto.get()
    categoria = entrada_categoria.get()
    
    if monto and categoria:
        try:
            monto = float(monto)
            guardar_gasto_csv(monto, categoria)
            print(f"Gasto guardado: ${monto} en {categoria}")
            entrada_monto.delete(0, tk.END)
            entrada_categoria.delete(0, tk.END)
            cargar_gastos()  # Actualizar la lista al agregar
        except ValueError:
            print("❌ El monto debe ser un número.")
    else:
        print("❌ Completá ambos campos.")

def cargar_gastos():
    lista_gastos.delete(0, tk.END)  # Limpiar lista
    if not os.path.exists(ARCHIVO):
        return
    with open(ARCHIVO, mode="r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            item = f"{fila['fecha']} | ${float(fila['monto']):.2f} | {fila['categoria']}"
            lista_gastos.insert(tk.END, item)

# Widgets para agregar gasto
tk.Label(ventana, text="Monto:").pack()
entrada_monto = tk.Entry(ventana)
entrada_monto.pack()

tk.Label(ventana, text="Categoría:").pack()
entrada_categoria = tk.Entry(ventana)
entrada_categoria.pack()

boton_agregar = tk.Button(ventana, text="Agregar gasto", command=agregar_gasto)
boton_agregar.pack(pady=10)

# Lista para mostrar gastos
lista_gastos = tk.Listbox(ventana, width=50)
lista_gastos.pack(pady=10)

# Botón para recargar lista (opcional)
boton_cargar = tk.Button(ventana, text="Actualizar lista", command=cargar_gastos)
boton_cargar.pack()

# Carga inicial de gastos
cargar_gastos()

ventana.mainloop()
