class Address:
    def __init__(self, Street: str = "", Barrio: str = "", Department: str = "") -> None:

        if type(Street) != str:
            print("Por favor ingrese un street valido.")
            return

        if type(Barrio) != str:
            print("Por favor ingrese un barrio valido.")
            return

        if type(Department) != str:
            print("Por favor ingrese una Department valido.")

        self._street = Street
        self._barrio = Barrio
        self._department = Department

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, new_street: int) -> None:
        if isinstance(new_street, str):
            self._street = new_street
        else:
            print("Por favor ingrese una street valida.")

    @property
    def barrio(self) -> str:
        return self.barrio

    @barrio.setter
    def barrio(self, new_barrio: int) -> None:
        if isinstance(new_barrio, str):
            self._barrio = new_barrio
        else:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, new_department: int) -> None:
        if isinstance(new_department, str):
            self._department = new_department
        else:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")

    def getInfo(self):
        return f"""\nCalle: {self._street}\nBarrio: {self._barrio}\nDepartamento: {self._department} """


Address_ex = Address("1str", "2str", "3str")
print(Address_ex.getInfo())
