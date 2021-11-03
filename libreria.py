import requests
from bs4 import BeautifulSoup
import csv


def obtenerCSV(url, id, nombreArchivo, tipo):
    # indicar la ruta
    url_page = url;

    # tarda 480 milisegundos
    page = requests.get(url_page).text 
    soup = BeautifulSoup(page, 'html.parser')

    # Obtenemos la tabla por un ID específico
    tabla = soup.find('table', attrs={tipo: id})
    #print(tabla)
    
    with open(nombreArchivo+ '.csv','w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        lista=[]
        for celda in tabla.find_all("th"):
            


            lista.append(celda.text)    
        writer.writerow(lista)      
        for fila in tabla.find_all("tr"):
            lista=[]
            for celda in fila.find_all('td'):
                lista.append(celda.text)
                print(celda.text)
            if(len(lista)!=0):
                writer.writerow(lista)  


import requests
from bs4 import BeautifulSoup
import csv


def obtenerCSV2(url, id, nombreArchivo, tipo,nombreColumna):
    # indicar la ruta
    url_page = url;

    # tarda 480 milisegundos
    page = requests.get(url_page).text 
    soup = BeautifulSoup(page, 'html.parser')

    # Obtenemos la tabla por un ID específico
    tabla = soup.find('table', attrs={tipo: id})
    #print(tabla)
    maximo=tabla.find('th','Máx.')
    
    
    #maximo = soup.find_all('th', attrs={'tipo': nombreColumna})
    return maximo

def obtenerLista(url, id, nombreArchivo, tipo,nombreAccion,nombreColumnaMax):
    url_page = url;

    # tarda 480 milisegundos
    page = requests.get(url_page).text 
    soup = BeautifulSoup(page, 'html.parser')

    # Obtenemos la tabla por un ID específico
    tabla = soup.find('table', attrs={tipo: id})
    #print(tabla)
    #maximo = soup.find_all('td', attrs={'data-field': nombreColumna})
    lista=[]
    indice=0
    for fila in tabla.find_all("th"):
        indice=indice+1
        if fila.text==nombreAccion:
            break

    indNom=0
    for fila in tabla.find_all("th"):
        indNom=indNom+1
        if fila.text==nombreColumnaMax:
            break

    indice2=0
    indNomb2=0
    lis=[]
    lisAcciones=[]
    for fila in tabla.find_all("tr"):
        indice2=0
        for celda in fila.find_all('td'):
            indice2=indice2+1
            if indice==indice2:
                lis.append(float(celda.text.replace(',', '.')))
            if indNom==indice2:
                lisAcciones.append(celda.text)

    
    return lisAcciones,lis