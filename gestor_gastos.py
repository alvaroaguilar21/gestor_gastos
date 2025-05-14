import csv
from datetime import datetime

ARCHIVO = "gastos.csv"

def cargar_datos():
    gastos = []
    try:
        with open(ARCHIVO, mode="r", newline="") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila["monto"] = float(fila["monto"])
                fila["fecha"] = datetime.strptime(fila["fecha"], "%Y-%m-%d")
                gastos.append(fila)
    except FileNotFoundError:
        pass  # Si no existe el archivo, empezamos con lista vacía
    return gastos

def guardar_gasto(monto, categoria, fecha):
    with open(ARCHIVO, mode="a", newline="") as archivo:
        campos = ["monto", "categoria", "fecha"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if archivo.tell() == 0:
            escritor.writeheader()  # Escribimos encabezado si es nuevo
        escritor.writerow({
            "monto": monto,
            "categoria": categoria,
            "fecha": fecha.strftime("%Y-%m-%d")
        })

def mostrar_menu():
    print("\n--- Gestor de Gastos Personales ---")
    print("1. Agregar gasto")
    print("2. Ver todos los gastos")
    print("3. Salir")

def agregar_gasto():
    try:
        monto = float(input("Monto del gasto: $"))
        categoria = input("Categoría (ej: comida, transporte, etc): ").strip()
        fecha_input = input("Fecha (YYYY-MM-DD) [Enter para hoy]: ").strip()
        fecha = datetime.today() if fecha_input == "" else datetime.strptime(fecha_input, "%Y-%m-%d")
        guardar_gasto(monto, categoria, fecha)
        print("✅ Gasto guardado correctamente.")
    except ValueError:
        print("❌ Error: formato de entrada inválido.")

def ver_gastos():
    gastos = cargar_datos()
    if not gastos:
        print("No hay gastos registrados.")
        return
    print("\n--- Lista de gastos ---")
    for g in gastos:
        print(f"{g['fecha'].date()} | ${g['monto']:>7.2f} | {g['categoria']}")

# --- Bucle principal ---
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()
    if opcion == "1":
        agregar_gasto()
    elif opcion == "2":
        ver_gastos()
    elif opcion == "3":
        print("👋 Hasta luego.")
        break
    else:
        print("❌ Opción no válida.")
