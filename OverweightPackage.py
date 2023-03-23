from Package import Package
from abc import ABC, abstractmethod


class OverweightPackage(Package):
    @abstractmethod
    def __init__(self, oid: int = 0, weight: float = 0.0, description: str = '', cost: float = 0.0, W_GR_100: float = 0.0, Costo_Sp: float = 2000, Sp: float = 0.0):
        self.Costo_Sp = Costo_Sp  # Valor costo del sobrepeso
        self.Sp = Sp  # Valor del sobrepeso (en Kg)
        super().__init__(oid, weight, description)
        self.Sp = self.weight - 30  # El sobrepeso es a partir de 30 kg
        self._cost = self.calculate()

    def calculate(self) -> float:
        calcular = (self.weight * self.W_GR_100 * 1000)
        if self.Sp > 1.0 and self.Sp < 10.0:  # 3000 para un rango entre 1 y 10s
            calcular += self.Sp * 3000
            return calcular

        elif self.Sp > 10.0:  # 10000 para un rango mayor que 20
            calcular += self.Sp * 10000
            return calcular

        def getInfo(self):  # inherited method # Polimorfism
            # return super().getInfo()
            return super().getInfo()+f"""\nCosto por sobrepeso: {self.Costo_Sp}\ncosto:{self._cost} """   # info + los nuevos atributos de la subclase


OverweightPackagexample = OverweightPackage(13, 68.6)

print(OverweightPackagexample.getInfo())
