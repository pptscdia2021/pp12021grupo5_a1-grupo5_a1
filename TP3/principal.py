import os
from pandas.core.frame import DataFrame
from CSV import CSV
from Entidades.departamento import Departamento
from Entidades.empleado import Empleado
from conexionMongo import cantidadElementos
from conexionMongo import crearBase
from funciones import ingresarFecha
from departamentodb import DepartamentoBD
from empleadodb import EmpleadoBD
from funciones import presioneTecla
from accion import accion

def ingresarOpcion():

    correcto=False
    num=0
    while(not correcto):
        try:
            num=int(input('Introducir el numero de la opcion a realizar: '))
            correcto=True
        except Exception as e:
            print("El valor a ingresar debe ser numerico")
            presioneTecla()
    return num


if __name__ == "__main__":
    salir=False
    opcion=0
    print("")
    os.system("cls")
    while not salir:
        print("OPCIONES")
        print("Para los puntos 3,4,5,6 se debe ejecutar primero el 1")
        print("Objetivo 1")
        print("1. Obtener datos de acciones de Bolsa de España y guardarlo en un archivo csv llamado bolsaMadrid.csv")
        print("2. Obtener datos de acciones de Yahoo Finance y guardarlo en un archivo csv llamado yahoo.csv")
        print("3. Mostrar datos de Bolsa de España en forma de Tabla")
        print("4. Mostrar datos de Yahoo Finance en forma de Tabla")
        print("Objetivo 2")
        print("5. Identificar 2 cotizaciones de mayor ganancia")
        print("6. Identificar 2 cotizaciones de mayor perdida")
        print("Objetivo 3")
        print("7. Comparativa de precios de cotización entre los dos orígenes de datos")
        print("Objetivo 4")
        print("8. Grafico -Comparativa de precios de cotización entre los dos orígenes de datos")
        print("Base De Datos")
        print("9. Obtener datos completos de los empleados")
        print("10. Obtener datos completos de los departamentos")
        print("11. Cantidad de Empleados de un genero determinado")
        print("12. Insertar Departamentos")
        print("13. Insertar Empleados")
        print("14. Borrar Empleado")
        print("15. Crear en MongoDB una base de datos y una colección con el mismo nombre. Cargar los datos del archivo csv denominado weatherHistory.csv")
        print("16. Mostrar cantidad de elementos cargados en la coleccion weatherHistory")
        print("17. Salir")
        
    
        opcion = ingresarOpcion()



        bolsaMadrid=CSV('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','id','ctl00_Contenido_tblAcciones')
        yahoo=CSV('https://es.finance.yahoo.com/world-indices/','class','W(100%)')

        print()
        print()
        if opcion == 1:
            bolsaMadrid.obtenerCSV('bolsaMadrid')
            print("Archivo creado exitosamente!")  
        elif opcion==2:
            yahoo.obtenerCSV('yahoo')
            print("Archivo creado exitosamente!")  
            
        elif opcion==3:
            print('ACCIONES DE LA BOLSA DE MADRID')
            print('------------------------------------------------------------------------------------------------')
            datos=bolsaMadrid.abrirCSV('bolsaMadrid')
            print(datos)
            
        elif opcion==4:
            print('ACCIONES DE LA BOLSA DE YAHOO FINANCE')
            print('------------------------------------------------------------------------------------------------')
            datos2=yahoo.abrirCSV('yahoo')
            print(datos2)
            
        elif opcion==5:
            datos=bolsaMadrid.abrirCSV('bolsaMadrid')#pd.read_csv('bolsaMadrid.csv', header=0, encoding = "ISO-8859-1")
            print("Las 2 cotizaciones de mayor ganancia son: ")
            print(accion.obtenerCotizacionesMayorGanancia(datos,2))
            
        elif opcion==6:
            datos=bolsaMadrid.abrirCSV('bolsaMadrid')#pd.read_csv('bolsaMadrid.csv', header=0, encoding = "ISO-8859-1")
            print("Las 2 cotizaciones de mayor perdida son: ")
            print(accion.obtenerCotizacionesMayorPerdida(datos,2))
            
        elif opcion==7:
            accion.comprarativaPrecios(yahoo,bolsaMadrid,False)
            
        elif opcion==8:
            accion.comprarativaPrecios(yahoo,bolsaMadrid,True)
        elif opcion==9:
            print("EMPLEADOS")
            for item in EmpleadoBD.obtenerEmpleados():
                print(item)
        elif opcion==10:
            print("DEPARTAMENTOS")
            for item in DepartamentoBD.obtenerDepartamentos():
                print(item)
        elif opcion==11:
            g='A'
            while(g.upper()!='F' and g.upper()!='M'):
                g=input('(M)Masculino, (F) Femenino : ')
            print("Cantidad: " + str(EmpleadoBD.obtenerCantidadEmpleadosPorGenero(g)));
        elif opcion==12:
            d=Departamento(input("Ingrese Nro Departamento: "),input("Ingrese Nombre Departamento: "))
            DepartamentoBD.agregarDepartamento(d)
            print("Departamento Ingresado con exito")
        elif opcion==13:
            e=Empleado(0,ingresarFecha(),input("Ingrese Nombre: "),input("Ingrese Apellido: "),input("Ingrese Genero: "),ingresarFecha())
            EmpleadoBD.agregarEmpleado(e)
            print("Empleado Ingresado con exito")
        elif opcion==14:
            cod=int(input("Ingrese codigo de Empleado a eliminar: "))
            if(EmpleadoBD.borrarEmpleado(cod)==0):
                print("El empleado ingresado, no se puede borrar, ya que no eexiste")
            else:
                print("Empleado Eliminado con exito")
        elif opcion==15:
            crearBase('weatherHistory','weatherHistory','./BASE DE DATOS/weatherHistory.csv')
        elif opcion==16:
            cantidadElementos('weatherHistory','weatherHistory')
        elif opcion == 17:
            salir=True
            os._exit(1)
        else:
            print ("Introduce un numero correcto")

        presioneTecla()
        print("")
        print("")
        print("")




