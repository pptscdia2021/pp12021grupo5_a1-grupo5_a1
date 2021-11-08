import pymongo as pym
import pandas as pd

#Conexión a MongoDB
client = pym.MongoClient('localhost',27017)
db = client['mongo']

#Colección
collection = db['income']

with open('encabezados.txt') as finput:
    column_names = finput.readline()
column_names

column_names_list = column_names.split(',')
column_names_list

#with open('income.txt')as finput:
with open('adult.data')as finput:
    for line in finput:
        row_list =line.rstrip('\n').split(',')
        row_dict = dict(zip(column_names_list,row_list))
        try:
            row_dict['age']= int(row_dict['age'])
            collection.insert_one(row_dict)
        except:
            pass
finput.close()

df = pd.read_table('adult.data', header = None, sep = ',')
df.columns=column_names_list
df

data = df.to_dict(orient = "records") 
collection.insert_many(data)

collection.count_documents({})

age39 = collection.find_one({'age':{'$eq' : 39}}) #alternatively, {'age': 39} can be used
print(age39)
