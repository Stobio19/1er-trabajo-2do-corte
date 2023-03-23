#  Class person
class Person:
    def __init__(self, code: int, name: str, last_name: str, age: str):
        if type(code) != int:
            print("\n¡Ingrese un valor válido")
            return

        if type(name) != str:
            print("\n¡El valor del nombre está incorrecto, ingrese un valor válido")
            return

        if type(last_name) != str:
            print("\n¡El valor del apellido está incorrecto, ingrese un valor válido")
            return

        if type(age) != str:
            print(
                "\n¡El valor ingresado para la edad es inválido!, por favor ingrese un nuevo valor")

        # Atributes
        self._code: int = code
        self._name: str = name
        self._last_name: str = last_name
        self._age: str = age

    @property
    def code(self) -> int:
        return (self._code)

    @code.setter
    def code(self, new_code: int) -> None:
        if (new_code, int):
            self._code = new_code
        else:
            print("\n¡El valor ingresado es inválido!, por favor ingrese un nuevo valor")

    @property
    def name(self) -> str:  # getter of name
        return (self._name)

    @name.setter  # setter of name
    def name(self, new_name: str) -> None:
        if (new_name, str):
            self._name = new_name
        else:
            print("\n¡Por favor ingrese un valor válido")

    @property
    def last_name(self) -> str:  # getter of last_name
        return (self._last_name)

    @last_name.setter  # setter of the last_name
    def last_name(self, new_last_name: str) -> None:
        if (new_last_name, str):
            _last_name = new_last_name
        else:
            print("\n¡Error!, por favor ingrese un valor válido")

    @property
    def age(self) -> str:  # getter of the age
        return (self._age)

    @age.setter  # setter of the age
    def age(self, new_age: str) -> None:
        if (new_age, str):
            _age = new_age
        else:
            print("\n¡¡Error en opción!!, por favor ingrese una opción válida")

    # __str__
    def getInfo(self):
        return f"""\n ID: {self._code}\n Name: {self._name}\n Last name: {self.last_name}\n Age: {self._age}"""


p = Person(12, "alvaro", "el barbaro", "19")
print(p.getInfo())
