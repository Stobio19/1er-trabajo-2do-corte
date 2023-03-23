# Comentarios
# Abstraer: identificar lo que nos interesa y separarlo de lo que no nos interesa
from abc import ABC, abstractmethod  # Import Library to Abstract Methods


class Package:  # Clase madre #Convención, nombre de la clase comienza con mayúscula
    # Constructor
    # Self: variable de instancia
    @abstractmethod
    def __init__(self, oid: int = 0, weight: float = 0.0, description: str = '', cost: float = 0.0, W_GR_100: float = 0.0):  # New Object
        if type(oid) != int:  # Validando el id
            print("\n¡El id está incorrecto, ingrese un id válido!")
            return

        if type(weight) != float and type(weight) != int:  # Validando el peso
            print("\n¡El peso está incorrecto, ingrese peso válido!")
            return

        if type(description) != str:  # Validando la descripción
            print("\n¡La descripción está incorrecta, ingrese un dato válido!")
            return

        self._oid: int = oid
        self._weight: float = weight
        self._description: str = description
        self.W_GR_100 = 1.0  # Gramo a 1.0s
        self._cost: float = self.calculate()  # Costo del envío

    # Publico -> accesible para todos
    # protegido _ -> solo debería acceder desde la propia clase y sus subclases
    # private _ -> solo es accesible para su propia clase

    # Getters / setters
    # get -> obtener (lectura)
    # set -> setear/establecer (escritura)

    # Getters

    @property
    def oid(self) -> int:  # Getter to obtain the id
        return self._oid

    # Setters
    # id
    @oid.setter
    def oid(self, new_oid) -> None:  # Modifying the atribute "id"
        # validating that the id is not negative
        if new_oid >= 0:
            self._oid = new_oid

        else:
            print("\n¡¡El id no puede ser menor que 0!!")

    @property
    # Peso
    def weight(self) -> float:  # get
        return self._weight

    @weight.setter
    def weight(self, new_weight) -> None:  # set
        if new_weight >= 0.0:
            self._weight = new_weight

        else:
            print("\n¡¡El peso no puede ser menor que 0!!")

    # Descripción

    @property
    def description(self) -> str:
        return self._description  # get

    @description.setter
    def description(self, new_description) -> None:  # set
        if type(new_description) != str:  # validating that it is atribute str
            print("\n¡¡No puede estar vacío!!")
        else:
            self._description = new_description

    @property
    def cost(self):  # Shipping value (Valor del envío)
        return self._cost  # get

    # Métodos

    # Calculate # Abstract Method

    @abstractmethod
    def calculate(self) -> float:  # Function to return shipping value
        pass

    # __str__

    def getInfo(self):  # getInfo: obtain the information // # Use f""" """
        return f"""\n ID: {self._oid}\n Weight: {self._weight}\n Description: {self._description}\n Cost: {self._cost}\n W_GR_100: {self.W_GR_100}\n  """


# Instanciar un objeto de la clase
# Creación de un objeto
person = Package(12, 67.5, 'Hola, soy samuel', 700.000, 80)
x = Package()
# print(person._oid)
# Accediendo a la información del método getInfo()
# person.set_oid(-1)  # Modifying the atribute id
# print(person.getInfo())
# print(person.get_oid())
# print(person.cost)
# person.weight = 600


# Class “StandardPackage”

# print(person.getInfo())
