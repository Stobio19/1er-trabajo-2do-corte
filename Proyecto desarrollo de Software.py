# Comentarios
# Abstraer: identificar lo que nos interesa y separarlo de lo que no nos interesa

class Package:  # Clase madre #Convención, nombre de la clase comienza con mayúscula
    # Constructor
    # Self: variable de instancia
    def __init__(self, oid: int = 0, weight: float = 0.0, description: str = '', cost: float = 0.0, W_GR_100: float = 0.0):  # New Object
        self.__oid = oid
        self.__weight = weight
        self.__description = description
        self.__cost = cost
        self.W_GR_100 = W_GR_100

    # Publico -> accesible para todos
    # protegido _ -> solo debería acceder desde la propia clase y sus subclases
    # private __ -> solo es accesible para su propia clase

    # Getters / setters
    # get -> obtener (lectura)
    # set -> setear/establecer (escritura)

    # Getters
    def get_oid(self):  # Getter to obtain the id
        return self.__oid

    # Setters
    def set_oid(self, new__oid):  # Modifying the atribute "id"
        # validating that the id is not negative
        if new__oid >= 0:
            self.__oid = new__oid

        else:
            print("\n¡¡El id no puede ser menor que 0!!")

    # Métodos

    def getInfo(self):  # getInfo: obtain the information // # Use f""" """
        return f"""\n ID: {self.__oid}\n Weight: {self.__weight}\n Description: {self.__description}\n Cost: {self.__cost}\n W_GR_100: {self.W_GR_100}\n  """


# Instanciar un objeto de la clase
# Creación de un objeto
person = Package(12, 67.5, 'Hola, soy samuel', 700.000, 80)

# Accediendo a la información del método getInfo()
# person.set_oid(-1)  # Modifying the atribute id
# print(person.getInfo())
# print(person.get_oid())
# print(person.cost)

# Class “StandardPackage”


class StandardPackage(Package):  # class inherits from Package class
    def __init__(self, oid: int = 0, weight: float = 0.0, description: str = '', cost: float = 0.0, W_GR_100: float = 0.0):
        super().__init__(oid, weight, description, cost,
                         W_GR_100)  # Define __init__ of the new class

    def getInfo(self):  # inherited method # Polimorfism
        # return super().getInfo()

        info = super().getInfo()

        return info + f""" """  # info + los nuevos atributos de la subclase


StandardPackageexample = StandardPackage(13, 68.5, 'xdxd', 800.000, 90)
print(StandardPackageexample)
print(StandardPackageexample.getInfo())
