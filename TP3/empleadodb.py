import pymysql
from Entidades.empleado import Empleado
from conexion import Conexion


class EmpleadoBD:

    def obtenerEmpleados():
        try:
            conexion = Conexion.conectar()
            try:
                empleados=[]
                with conexion.cursor() as cursor:
                    # En este caso no necesitamos limpiar ningún dato
                    cursor.execute("SELECT * FROM employees limit 10;")
        
                    # Con fetchall traemos todas las filas
                    employees = cursor.fetchall()
        
                    # Recorrer e imprimir
                    for emp in employees:
                        e=Empleado(emp[0],emp[1],emp[2],emp[3],emp[4],emp[5])
                        empleados.append(e)
                    return empleados
            finally:
                conexion.close()
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)

    def obtenerCantidadEmpleadosPorGenero(genero):
        try:
            conexion = Conexion.conectar()
            try:
                with conexion.cursor() as cursor:
                    # En este caso no necesitamos limpiar ningún dato
                    cursor.execute("select count(*) Cantidad  from employees where gender=%s;",genero.upper())
        
                    # Con fetchall traemos todas las filas
                    cantidad = cursor.fetchone()
        
                    # Recorrer e imprimir
                    return cantidad[0]
            finally:
                conexion.close()
            

        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)

    def agregarEmpleado(emp):
        try:
            conexion = Conexion.conectar()
            try:
                with conexion.cursor() as cursor:
                    #sentencia="INSERT INTO employees ('emp_no','birth_date','first_name','last_name','gender','hire_date')) VALUES (%s,%s,%s,%s,%s,%s);"
                    sentencia="INSERT INTO employees SELECT MAX(emp_no)+1, %s,%s,%s,%s,%s FROM employees;"
                    #valores=(emp.getEmpNo(), emp.getFechaNacimiento(), emp.getNombre(), emp.getApellido(),emp.getGenero(),emp.getFechaContratacion())
                    valores=(emp.getFechaNacimiento(), emp.getNombre(), emp.getApellido(),emp.getGenero(),emp.getFechaContratacion())
                    cursor.execute(sentencia,valores)
        
                    # Con fetchall traemos todas las filas
                    departamentos = cursor.fetchall()
        
                    conexion.commit()
            finally:
                conexion.close()
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)

    def borrarEmpleado(codEmp):
        try:
            conexion = Conexion.conectar()
            try:
                with conexion.cursor() as cursor:
                    #sentencia="INSERT INTO employees ('emp_no','birth_date','first_name','last_name','gender','hire_date')) VALUES (%s,%s,%s,%s,%s,%s);"
                    sentencia="DELETE FROM employees where  emp_no=%s;"
                    valores=(codEmp)
                    a=cursor.execute(sentencia,valores)
        
                    # Con fetchall traemos todas las filas
                    #departamentos = cursor.fetchall()
        
                    conexion.commit()

                    return a
            finally:
                conexion.close()
        
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Ocurrió un error al conectar: ", e)