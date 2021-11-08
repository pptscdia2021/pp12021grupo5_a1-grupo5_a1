import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

class CSV:
    

    def __init__(self, url):
        self.url_page=url

    
    def obtenerCSV(self,tipo, id,nombreArchivo):
        page = requests.get(self.url_page).text 
        soup = BeautifulSoup(page, 'html.parser')

        tabla = soup.find('table', attrs={tipo: id})
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