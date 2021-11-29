class Departamento:
    def __init__(self):
        self.__nro=""
        self.__nombre=""
        
    def __init__(self, nro,nom):
        self.__nro=nro
        self.__nombre=nom

    def setNro(self, nro):
        self.__nro=nro

    def getNro(self):
        return self.__nro

    def setNombre(self, nombre):
        self.__nombre=nombre;

    def getNombre(self):
        return self.__nombre
    

    def __str__(self):
        return "Nro: " + str(self.getNro()) + " Nombre: "  + self.getNombre()