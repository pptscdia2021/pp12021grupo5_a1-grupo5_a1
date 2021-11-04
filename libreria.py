import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def obtenerCSV(url, id, nombreArchivo, tipo):
    # indicar la ruta
    url_page = url;

    # tarda 480 milisegundos
    page = requests.get(url_page).text 
    soup = BeautifulSoup(page, 'lxml')

    # Obtenemos la tabla por un ID específico
    tabla = soup.find('table', attrs={tipo: id})
    #print(tabla)
    
    with open(nombreArchivo+ '.csv','w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        lista=[]
        for celda in tabla.find_all("th"):
            lista.append(celda.text.replace('\n',''))    
        writer.writerow(lista)      
        for fila in tabla.find_all("tr"):
            lista=[]
            for celda in fila.find_all('td'):
                lista.append(celda.text)
              #  print(celda.text)
            if(len(lista)!=0):
                writer.writerow(lista)  

def mostrarTabla(nombreArchivo):
   # df=pd.read_csv(nombreArchivo, sep="\t", encoding = "ISO-8859-1")
    datos=pd.read_csv(nombreArchivo, header=0, encoding = "ISO-8859-1")
    print(datos)
#

