from datetime import date, datetime

class Empleado:
    def __init__(self):
        self.__emp_no=0
        self.__birth_date=date.today()
        self.__first_name=""
        self.__last_name=""
        self.__gender=''
        self.__hire_date=date.today()

    def __init__(self, nro,fechan,nom, ap,gen,fechacon):
        self.__emp_no=nro
        self.__birth_date=fechan
        self.__first_name=nom
        self.__last_name=ap
        self.__gender=gen
        self.__hire_date=fechacon
    
    def setEmpNo(self, empNro):
        self.__emp_no=empNro

    def getEmpNo(self):
        return self.__emp_no

    def setFechaNacimiento(self, fe):
        self.__birth_date=fe;

    def getFechaNacimiento(self):
        return self.__birth_date

    def setNombre(self, nombre):
        self.__first_name=nombre;

    def getNombre(self):
        return self.__first_name
    
    def setApellido(self, apellido):
        self.__last_name=apellido;

    def getApellido(self):
        return self.__last_name

    def setGenero(self, genero):
        self.__gender=genero;

    def getGenero(self):
        return self.__gender

    def obtenerGenero(self):
        if (self.__gender=='M'):
            return 'Masculino'
        else:
            return 'Femenino'

    def setFechaContratacion(self, fechaContratacion):
        self.__hire_date=fechaContratacion;

    def getFechaContratacion(self):
        return self.__hire_date

    def __str__(self):
        #return "Nro: " + str(self.getEmpNo()) + " Nombre: " + self.getApellido() +", " + self.getNombre() + " Fecha Nacimiento: " + self.getFechaNacimiento()
        return "Nro: " + str(self.getEmpNo()) + " Nombre: " + self.getApellido() +", " + self.getNombre() + " Fecha Nacimiento: " + str(self.getFechaNacimiento()) + " Genero: " + self.obtenerGenero() + " Fecha Contratacion: " + str(self.getFechaContratacion())