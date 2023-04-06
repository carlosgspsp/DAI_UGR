import random
import re

def palabraMayuscula(cadena):
    return bool(re.match(r"[\w\s]+[A-Z]", cadena))

def correoValido(cadena):
    return bool(re.match(r"^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,3})$", cadena))

def tarjetaCredito(cadena):
    return bool(re.match(r"^\d{4}([\ -]?)\d{4}\1\d{4}\1\d{4}$", cadena))


if __name__ == '__main__':

    cadena1 = "Carlos g"
    cadena2 = "carlosgsgmail.com"
    cadena3 = "1234 5678 9012 3456"
    print(palabraMayuscula(cadena1))
    print(correoValido(cadena2))
    print(tarjetaCredito(cadena3))
    



