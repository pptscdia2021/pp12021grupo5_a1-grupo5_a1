from CSV import CSV





def ingresarOpcion():
    correcto=False
    num=0
    while(not correcto):
        num=int(input('Introducir el numero de la opcion a realizar: '))
        correcto=True
    return num

salir=False
opcion=0
print("")
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
    print("7. Salir")
    
 
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





