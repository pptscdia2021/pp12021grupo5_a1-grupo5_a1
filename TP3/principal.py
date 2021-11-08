from CSV import CSV
from accion import accion
from cotizacion import cotizacion

def ingresarOpcion():
    correcto=False
    num=0
    while(not correcto):
        num=int(input('Introducir el numero de la opcion a realizar: '))
        correcto=True
    return num

if __name__ == "__main__":
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
        print("Objetivo 3")
        print("7. Comparativa de precios de cotización entre los dos orígenes de datos")
        print("Objetivo 4")
        print("8. Grafico -Comparativa de precios de cotización entre los dos orígenes de datos")
        print("10. Salir")
        
    
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
            accionesMadrid=['REPSOL','TELEFONICA','BBVA','MAPFRE','B.SANTANDER']
            accionesyahoo=['REP.MC','TEF','BBVA','MAP.MC','SAN']
            
            print()
            accion.obtenerCotizacionesYahoo(accionesyahoo,accionesMadrid)   #Genera el archivo yahoocomp
            print("Yahoo Finance")
            print("--------------------------")
            yahoo=yahoo.abrirCSV('yahoocomp')
            print(yahoo[['Nombre','Close']])
            print()
            datos=bolsaMadrid.abrirCSV('bolsaMadrid')
            datos["Últ."]=datos["Últ."].str.replace(',', '.').astype(float)
            dolar=cotizacion.obtenerCotizacion("EURUSD=X")
            datos["Últ."]=datos["Últ."]*dolar
            datos=datos.rename(columns={'Últ.':'Valor'})
            accionesbolsaMadrid=datos[datos.Nombre.isin(accionesMadrid)]
            print("Valor Euro:" + str(dolar))
            print()
            print("Acciones Bolsa de Madrid")
            print("--------------------------")
            print(accionesbolsaMadrid[['Nombre','Valor']])
            print()
            print("Tabla Comparativa en Dolares")
            print("--------------------------")
            dfcomp=accion.tablaComparacion(accionesbolsaMadrid,yahoo)
            print(dfcomp)
        elif opcion==8:
            print("Tabla Comparativa en Dolares")
            print("--------------------------")

            print(dfcomp)
            
            accion.graficar(dfcomp,'Nombre','Comparación 5 acciones','grafico.png')

        
        elif opcion == 10:
            salir=True
        else:
            print ("Introduce un numero correcto")


        print("")
        print("")
        print("")




