import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import yfinance as yf
from datetime import datetime,timedelta

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
            lista.append(celda.text.replace('\n',''))    
        writer.writerow(lista)      
        for fila in tabla.find_all("tr"):
            lista=[]
            for celda in fila.find_all('td'):
                lista.append(celda.text)
                #print(celda.text)
            if(len(lista)!=0):
                writer.writerow(lista)  

def mostrarTabla(nombreArchivo):
       # df=pd.read_csv(nombreArchivo, sep="\t", encoding = "ISO-8859-1")
    datos=pd.read_csv(nombreArchivo, header=0, encoding = "ISO-8859-1")
    print(datos)


def obtenerCotizacionesYahoo(acciones, accionesbolsamadrid):
    lista=list()
    #ahora = datetime.now()
    #ayer = ahora - timedelta(days=1)
    #for accion in acciones:
    #    df=yf.download(accion, period="1d")
    #    print(df)

    #with open('yahoocomp'+ '.csv','w', newline='') as csv_file:
    #    writer = csv.writer(csv_file)
            # lista.append('Nombre')
       # lista.append('Cierre')
       # writer.writerow(lista)   
    #for accion in acciones:
    for indice in range(0, len(acciones)):
        df=yf.download(acciones[indice],group_by='ticker', period="1d")
        df['Accion']=accionesbolsamadrid[indice]
        lista.append(df)
    
    dff=pd.concat(lista)
    dff.to_csv('yahoocomp.csv')
    


    
        #df=yf.download(accion, start=ayer, end=ahora,group_by="ticker")
        

    #yf.ticker(accion)
    #df=yf.download("EURUSD=X", start=datetime.now().strftime('%Y-%m-%d'), end=datetime.now().strftime('%Y-%m-%d'),group_by="ticker")
    #return lista


def obtenerCotizacionEuro():
    dol=yf.Ticker("EURUSD=X")
    #df=yf.download("EURUSD=X", start="2021-09-03", end="2021-09-04",group_by="ticker")
    return dol.info['ask']












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