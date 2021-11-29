import pymysql


class Conexion:

    def conectar():
        try:
	        return pymysql.connect(host='localhost', user='root', password='030302', db='employees')
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	        print("Ocurrió un error al conectar: ", e)
        