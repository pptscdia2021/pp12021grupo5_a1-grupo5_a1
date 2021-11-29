import pymysql
from Entidades.departamento import Departamento
from conexion import Conexion


class DepartamentoBD:

    def obtenerDepartamentos():
        try:
            conexion = Conexion.conectar()
            try:
                resDepartamentos=[]
                with conexion.cursor() as cursor:
                    # En este caso no necesitamos limpiar ningún dato
                    cursor.execute("select * from departments;")
        
                    # Con fetchall traemos todas las filas
                    departamentos = cursor.fetchall()
        
                    # Recorrer e imprimir
                    for dep in departamentos:
                        d=Departamento(dep[0],dep[1])
                        resDepartamentos.append(d)
                    return resDepartamentos
            finally:
                conexion.close()
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)


    def agregarDepartamento(dep):
        try:
            conexion = Conexion.conectar()
            try:
                resDepartamentos=[]
                with conexion.cursor() as cursor:
                    sentencia="INSERT INTO departments (dept_no, dept_name) VALUES (%s,%s);"
                    valores=(dep.getNro(), dep.getNombre())

                    cursor.execute(sentencia,valores)
        
                    # Con fetchall traemos todas las filas
                    departamentos = cursor.fetchall()
        
                    conexion.commit()
            finally:
                conexion.close()
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)