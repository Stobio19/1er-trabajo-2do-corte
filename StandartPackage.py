from Package import Package
from abc import ABC, abstractmethod


class StandardPackage(Package):  # class inherits from Package class
    @abstractmethod
    def __init__(self, oid: int = 0, weight: float = 0.0, description: str = '', cost: float = 0.0, cuota_fija: float = 1000):
        # Primero se declaran las variables de la subclase
        self.cuota_fija: float = cuota_fija
        super().__init__(oid, weight, description)  # Define __init__ of the new class

    # Methods

    @abstractmethod
    def calculate(self) -> float:  # Function to return shipping value
        return (self.weight * self.W_GR_100 * 1000) + self.cuota_fija

    def getInfo(self):  # inherited method # Polimorfism
        # return super().getInfo()
        info = super().getInfo()
        return info+f"""\nCuota fija: {self.cuota_fija}\ncosto:{self.calculate() } """   # info + los nuevos atributos de la subclase


StandardPackageexample = StandardPackage(13, 68.3)
# print(StandardPackageexample)
# print(StandardPackageexample.getInfo())
print(StandardPackageexample.getInfo())
