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


def obtenerCSV3(url, id, nombreArchivo, tipo):
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
            if(len(lista)!=0):
                writer.writerow(lista)  

def obtener2Maximos(url, id, nombreArchivo, tipo,nombreColumna):
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
    for fila in tabla.find_all("tr"):
        indice=indice+1
        if fila.text==nombreColumna:
            break
    indice2=0
    lis=[]
    for fila in tabla.find_all("tr"):
        indice2=indice2+1
        for celda in fila.find_all('td'):
            if indice==indice2:
                lis.append(celda.text)
    
    
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
            if(len(lista)!=0):
                writer.writerow(lista)  





    Max_ind1 = maxAcciFloat.index(max(maxAcciFloat))
    Max_ind2 = maxAcciFloat.index(maxAcciFloat[-1])
    ind1 = maxAcciFloat.index(min(maxAcciFloat))
    ind2 = maxAcciFloat.index((maxAcciFloat[a]))

def mostrarTabla(archivo):
    with open(archivo+'.csv', newline='') as File:  
        reader = csv.DictReader(File)
        for row in reader:
            print(row)




def mostrarTabla2(archivo):
    with open(archivo+'.csv', newline='') as File:  
        reader = csv.DictReader(File)
        for row in reader:
            print(row[1], row[2])



def Pandas(archivo):
    datos=pd.read_csv(archivo + '.csv', header=0)
    print(datos)

# Abrimos el csv con append para que pueda agregar contenidos al final del archivo