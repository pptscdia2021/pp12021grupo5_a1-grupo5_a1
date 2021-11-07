from libreria import obtenerCSV
import csv
import pandas as pd

print("OBJETIVO 3")
print("*************************************************************")

obtenerCSV('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','ctl00_Contenido_tblAcciones','archivo','id')

obtenerCSV('https://es.finance.yahoo.com/world-indices/','W(100%)','archivo2','class')

df= pd.read_csv('archivo.csv')#leer el csv con pandas
dj= pd.read_csv('archivo2.csv')

pd.merge(df,dj)
