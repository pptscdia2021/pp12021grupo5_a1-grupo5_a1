
from os import sep
from libreria import  obtenerCSV,obtenerCotizacionEuro,obtenerCotizacionesYahoo

import pandas as pd


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
 


    print()
    print()
    if opcion == 1:
        obtenerCSV('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','ctl00_Contenido_tblAcciones','bolsaMadrid','id')
        print("Archivo creado exitosamente!")        
    elif opcion == 2:
        obtenerCSV('https://es.finance.yahoo.com/world-indices/','W(100%)','yahoo','class')
        print("Archivo creado exitosamente!")        
    elif opcion == 3:
        print('ACCIONES DE LA BOLSA DE MADRID')
        print('------------------------------------------------------------------------------------------------')
        datos=pd.read_csv('bolsaMadrid.csv', header=0, encoding = "ISO-8859-1")
        datos["% Dif."]=datos["% Dif."].str.replace(',', '.').astype(float)
        print(datos)
    elif opcion == 4:
        print('ACCIONES DE LA BOLSA DE YAHOO FINANCE')
        print('------------------------------------------------------------------------------------------------')
        datos2=pd.read_csv('yahoo.csv', header=0, encoding = "ISO-8859-1")
        print(datos2)
    elif opcion==5:
        datos=pd.read_csv('bolsaMadrid.csv', header=0, encoding = "ISO-8859-1")
        datos["% Dif."]=datos["% Dif."].str.replace(',', '.').astype(float)
        dfordenado=datos.sort_values(by="% Dif.", ascending=False)
        print("Las 2 cotizaciones de mayor ganancia son: ")
        print(dfordenado.head(2)[["Nombre","% Dif."]])
    elif opcion==6:
        datos=pd.read_csv('bolsaMadrid.csv', header=0, encoding = "ISO-8859-1")
        datos["% Dif."]=datos["% Dif."].str.replace(',', '.').astype(float)
        dfordenado=datos.sort_values(by="% Dif.", ascending=False)
        print("Las 2 cotizaciones de mayor perdida son: ")
        print(dfordenado.tail(2)[["Nombre","% Dif."]])
    elif opcion==7:
        accionesMadrid=['REPSOL','TELEFONICA','BBVA','MAPFRE','B.SANTANDER']
        accionesyahoo=['REP.MC','TEF','BBVA','MAP.MC','SAN']
        
        print()
        obtenerCotizacionesYahoo(accionesyahoo,accionesMadrid)
        print("Acciones Yahoo")
        print("--------------------------")
        datos2=pd.read_csv('yahoocomp.csv', header=0, encoding = "ISO-8859-1")
        print(datos2[['Accion','Close']])
        print()



        datos=pd.read_csv('bolsaMadrid.csv', header=0, encoding = "ISO-8859-1")
        datos["Últ."]=datos["Últ."].str.replace(',', '.').astype(float)
        dolar=obtenerCotizacionEuro()
        datos["Últ."]=datos["Últ."]*dolar
        accionesbolsaMadrid=datos[datos.Nombre.isin(accionesMadrid)]
        print("Valor Euro:" + str(dolar))
        print()
        print("Acciones Bolsa de Madrid")
        print("--------------------------")
        print(accionesbolsaMadrid[['Nombre','Últ.']])
  
        


    
    elif opcion == 10:
        salir=True
    else:
        print ("Introduce un numero correcto")



    
        
    print("")
    print("")
    print("")