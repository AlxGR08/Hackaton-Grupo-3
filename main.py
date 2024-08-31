#3-resta-anel
def resta(a, b):
    r = a-b
    return r

def division():
    a = float(input("Ingrese el primer número (dividendo): "))
    b = float(input("Ingrese el segundo número (divisor): "))

    if b == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = a / b
        print(f"El resultado de {a} dividido por {b} es: {resultado}")

division()


