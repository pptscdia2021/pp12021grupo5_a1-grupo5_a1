import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='030302',
                             db='employees')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)


try:
    conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='030302',
                             db='employees')
    try:
        with conexion.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("SELECT * FROM employees;")
 
            # Con fetchall traemos todas las filas
            employees = cursor.fetchall()
 
            # Recorrer e imprimir
            for emp in employees:
                print(emp)
    finally:
        conexion.close()
    
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

try:
    conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='employees')
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT emp_no, last_name FROM employees WHERE gender ='F';"
            cursor.execute(consulta)
 
            # Con fetchall traemos todas las filas
            employees = cursor.fetchall()
 
            # Recorrer e imprimir
            for emp in employees:
                print(emp)
    finally:
        conexion.close()
    
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)
