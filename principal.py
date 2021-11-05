
from os import sep
from libreria import  obtenerCSV

import pandas as pd
import numpy as np


print("OBJETIVO 1")
print("*************************************************************")

obtenerCSV('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','ctl00_Contenido_tblAcciones','archivo','id')

obtenerCSV('https://es.finance.yahoo.com/world-indices/','W(100%)','archivo2','class')

print()
print()
print()
print()    
print('ACCIONES DE LA BOLSA DE MADRID')
print('------------------------------------------------------------------------------------------------')
datos=pd.read_csv('archivo.csv', header=0, encoding = "ISO-8859-1")
print(datos)
print()
print()
print()
print()
print('ACCIONES DE LA BOLSA DE finance yahoo')
print('------------------------------------------------------------------------------------------------')
datos2=pd.read_csv('archivo2.csv', header=0, encoding = "ISO-8859-1")
print(datos2)
print()
print()
print()
print()
print("OBJETIVO 2")
print("*************************************************************")

datos["% Dif."]=pd.to_numeric(datos["% Dif."].str.replace(',', '.'))


print(datos["% Dif."].min().__index__)


dfordenado=datos.sort_values(by="% Dif.", ascending=False)



print("Las 2 cotizaciones de mayor ganancia son: ")
print(dfordenado.head(2)["Nombre"],dfordenado.head(2)["% Dif."])
print()
print("Las 2 cotizaciones de menor ganancia son: ")
print(dfordenado.tail(2)["Nombre"],dfordenado.tail(2)["% Dif."])







#mostrarTabla('archivo2.csv')



