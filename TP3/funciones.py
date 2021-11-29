from datetime import datetime
import os

def presioneTecla():
    print()
    print("Presion una Tecla para continuar")
    input()
    os.system("cls")

def ingresarFecha():
    try:
        dia=int(input("Ingresar Dia: "))
        mes=int(input("Ingresar Mes: "))
        año=int(input("Ingresar Año: "))
        return datetime(año,mes,dia)
    except Exception as e:
            print("El valor a ingresar debe ser numerico")