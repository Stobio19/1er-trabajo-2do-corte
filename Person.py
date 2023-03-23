class Person:
    def __init__(self, code: int, name: str, last_name: str):
        if type(code) != int:
            print("\n¡Ingrese un valor válido")
            return

        if type(name) != str:
            print("\n¡El valor del nombre está incorrecto, ingrese un valor válido")
            return

        if type(last_name) != str:
            print("\n¡El valor del apellido está incorrecto, ingrese un valor válido")
            return

        self.code: int = code
        self.name: str = name
        self.last_name: str = last_name
