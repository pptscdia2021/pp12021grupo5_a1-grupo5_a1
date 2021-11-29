import pymongo
import pandas as pd


def conectarseMongo():
    return pymongo.MongoClient('localhost',27017)


def crearBase(nombreBase, nombreColeccion, direccionArchivoCSV):

#Conexión a MongoDB
    client = conectarseMongo()
    db = client[nombreBase]

#Colección
    collection = db[nombreColeccion]

    with open(direccionArchivoCSV, newline='') as finput:
        column_names = finput.readline()
        column_names_list = column_names.split(',')

        for line in finput:
            row_list =line.rstrip('\n').split(',')
            row_dict = dict(zip(column_names_list,row_list))
            try:
                collection.insert_one(row_dict)
            except:
                pass

def cantidadElementos(nombreBase, nombreColeccion):
    client = conectarseMongo()
    db = client[nombreBase]

    collection = db[nombreColeccion]

    if collection.count()>0:
        print('Cantidad de registros ingresados en la coleccion: ', collection.count())
    else:
        print('No se ingreso ningun dato en la coleccion')