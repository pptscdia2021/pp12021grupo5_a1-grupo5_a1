
from os import sep
from libreria import mostrarTabla, obtenerCSV #,obtenerCSV2,obtenerLista

import pandas as pd



#obtenerCSV('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','ctl00_Contenido_tblAcciones','archivo','id')

obtenerCSV('https://es.finance.yahoo.com/world-indices/','W(100%)','archivo2','class')


mostrarTabla('archivo.csv')

mostrarTabla('archivo2.csv')






#lista, lista2=obtenerLista('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','ctl00_Contenido_tblAcciones','archivo','id','Máx.','Nombre')

#lista, lista2=obtenerLista('https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000','ctl00_Contenido_tblAcciones','archivo','id','% Dif.','Nombre')


#indiceMax1=lista2.index(max(lista2))
#indiceMax2=lista2.index(min(lista2))

#print("Nombre: ",lista[indiceMax1] ," Max: ", lista2[indiceMax1])
#print("Nombre: ",lista[indiceMax2] ," Min: ", lista2[indiceMax2])

#df = pd.read_csv('archivo.csv')
#print(df)







#print("Nombre: ", lista[Max1] , "Valor:", lista2[Max1])


#mostrarTabla('archivo2')

#import pandas as pd
#datos=pd.read_csv('arch2.csv',sep=',')
#print(datos)