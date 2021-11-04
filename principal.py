
from os import sep
from libreria import mostrarTabla, obtenerCSV

import pandas as pd




print("OBJETIVO 1")
print("*************************************************************")

obtenerCSV('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','ctl00_Contenido_tblAcciones','archivo','id')

obtenerCSV('https://es.finance.yahoo.com/world-indices/','W(100%)','archivo2','class')


print('ACCIONES DE LA BOLSA DE MADRID')
print('------------------------------------------------------------------------------------------------')
mostrarTabla('archivo.csv')

print('ACCIONES DE LA BOLSA DE finance yahoo')
print('------------------------------------------------------------------------------------------------')
mostrarTabla('archivo2.csv')



