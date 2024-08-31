import os

#Suma David
def suma(a,b):
    c=a+b
    print(c)

#3-resta-anel
def resta(a, b):
    r = a-b
    print(r)

#Division
def division(a,b):
    if b == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = a / b
        print(f"El resultado de {a} dividido por {b} es: {resultado}")

#Multiplicar
def multiplicar(a, b):
    print(a * b)

def limpiar_consola():
    # Limpia la consola dependiendo del sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        # Solicita al usuario que ingrese una operación
        n = input("Ingrese una operación (o presione 'c' para borrar): ")

        lista = n.split()
        nro1 = int(lista[0])
        nro2 = int(lista[2])
        operador = lista[1]
        

        if operador == "+":
            suma(nro1,nro2)
        elif operador == "-":
            resta(nro1,nro2)
        elif operador == "*":
             multiplicar(nro1,nro2)
        elif operador == "/":
            division(nro1,nro2)

        # Verifica si el usuario desea borrar la operación
        borrar = input("Quieres borrar la operacion (c/n): ")
        if borrar.lower() == 'c':
            limpiar_consola()

        # Verifica si el usuario desea salir
        salir = input("¿Desea realizar otra operación? (s/n): ").lower()
        if salir != 's':
            print("Saliendo de la calculadora.")
            break

main()