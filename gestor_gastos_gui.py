import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Gastos")
ventana.geometry("400x300")  # Ancho x Alto

# Lista para guardar los gastos
gastos = []

# Función para manejar el clic del botón
def agregar_gasto():
    monto = entrada_monto.get()
    categoria = entrada_categoria.get()
    
    if monto and categoria:
        try:
            monto = float(monto)
            gasto = {"monto": monto, "categoria": categoria}
            gastos.append(gasto)
            print(f"Gasto agregado: {gasto}")
            entrada_monto.delete(0, tk.END)
            entrada_categoria.delete(0, tk.END)
        except ValueError:
            print("El monto debe ser un número.")
    else:
        print("Completá ambos campos.")


# Etiqueta y entrada para el monto
etiqueta_monto = tk.Label(ventana, text="Monto:")
etiqueta_monto.pack()
entrada_monto = tk.Entry(ventana)
entrada_monto.pack()

# Etiqueta y entrada para la categoría
etiqueta_categoria = tk.Label(ventana, text="Categoría:")
etiqueta_categoria.pack()
entrada_categoria = tk.Entry(ventana)
entrada_categoria.pack()

# Botón para agregar gasto
boton_agregar = tk.Button(ventana, text="Agregar gasto", command=agregar_gasto)
boton_agregar.pack(pady=10)


# Ejecutar la app
ventana.mainloop()