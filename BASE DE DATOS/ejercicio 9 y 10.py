import pymongo
import pandas as pd

#Conexión a MongoDB
client = pymongo.MongoClient('localhost',27017)
db = client['mongo']

#Colección
collection = db['income']

with open('./BASE DE DATOS/weatherHistory.csv', newline='') as finput:
    column_names = finput.readline()
    column_names_list = column_names.split(',')

    for line in finput:
        row_list =line.rstrip('\n').split(',')
        row_dict = dict(zip(column_names_list,row_list))
        try:
            collection.insert_one(row_dict)
        except:
            pass

if collection.count()>0:
    print('Cantidad de registros ingresados en la coleccion: ', collection.count())
else:
    print('No se ingreso ningun dato en la coleccion')