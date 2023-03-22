from Package import Package
from abc import ABC, abstractmethod


class OverweightPackage(Package):
    @abstractmethod
    def __init__(self, oid: int = 0, weight: float = 0.0, description: str = '', cost: float = 0.0, W_GR_100: float = 0.0, Costo_Sp: float = 2000, Sp: float = 0.0):
        self.Costo_Sp = Costo_Sp  # Valor costo del sobrepeso
        self.Sp = Sp  # Valor del sobrepeso (en Kg)
        super().__init__(oid, weight, description)
        self.Sp = self.weight - 30  # El sobrepeso es a partir de 30 kg
        self.cost = self.calculate()

        @abstractmethod
        def calculate(self) -> float:
            calcular = (self.weight * self.W_GR_100 * 1000)
            if (self.Sp > 1 or self.Sp < 10):  # 3000 para un rango entre 1 y 10
                calcular += self.Sp * 3000

            elif (self.Sp > 11 or self.Sp < 20):  # 5000 para un rango entre 11 y 20
                calcular += self.Sp * 5000

            else (self.Sp > 20):  # 10000 para un rango mayor que 20
                calcular += self.Sp * 10000
