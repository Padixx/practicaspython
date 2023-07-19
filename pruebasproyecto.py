
while True:
    nombre = input("¿Cuál es su nombre? ")
    if nombre.isalpha():
        break
    else:
        print("Error, no ingreso ningun valor o no coloco su nombre usando solo letras") #No nos deja avanzar al siguiente punto si no se coloca el valor solcitiado

while True:
    apellidopaterno = input("¿Cuál es su apellido paterno? ")
    if apellidopaterno.isalpha():
        break
    else:
        print("Error, no ingreso ningun valor o no coloco su apellido paterno usando solo letras")

while True:
    apellidomaterno = input("¿Cuál es su apellido materno? ")
    if apellidomaterno.isalpha():
        break
    else:
        print("Error, no ingreso ningun valor o no coloco su apellido materno usando solo letras")

while True:
    edad = (input("Indique su edad: ")) #Varible int = número entero sin decimal
    if  edad.isdigit():
        break
    else:
        print("Error, no ingreso ningun valor numérico o coloco un número con decimales, vuelva a intentarlo")

while True:
    try:
        peso = float(input("Introduzca su peso en KG (máximo 1 decimal): "))
        break
    except ValueError:
        print("Error, no ingreso algún valor numérico, vuelva a intentarlo")

while True:
    try:
        estatura = float(input("Proporcione su estatura: "))
        break
    except ValueError:
        print("Error, no ingreso algún valor numérico, vuelva a intentarlo")

print("")
print("")
print("Resultados de la calculadora de IMC (Índice de Masa Corporal)")
print("Nombre: " + nombre)
print("Apellido paterno: " + apellidopaterno)
print("Apellido materno: " + apellidomaterno)
print("Edad: " + str(edad) + "años")
print("Peso: " + str(peso))
print("Estatura: " + str(estatura))


