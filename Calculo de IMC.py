# CALCULADORA DE INDICE DE MASA CORPORAL

while True: #while true que no nos permitira avanzar hasta tener la condicion verdadera
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
    edad = (input("Indique su edad: ")) 
    if  edad.isdigit():
        break
    else:
        print("Error, no ingreso ningun valor numérico o coloco un número con decimales, vuelva a intentarlo")

while True: #para el peso y estatura utilize try, así como la variable float la cual considera numeros con decimales
    try:
        peso = float(input("Introduzca su peso en KG (máximo 1 decimal): "))
        break
    except ValueError:
        print("Error, no ingreso algún valor numérico, vuelva a intentarlo")

while True:
    try:
        estatura = float(input("Proporcione su estatura en metros: "))
        break
    except ValueError:
        print("Error, no ingreso algún valor numérico, vuelva a intentarlo")


# FORMULA PARA SACAR EL IMC, PESO (EN KG) / ESTATURA (METROS) , ELEVADO AL CUADRADO
IMC = peso / estatura**2 

print("")
print("")
print("Resultados de la calculadora de IMC (Índice de Masa Corporal)")
print("Nombre: " + nombre)
print("Apellido paterno: " + apellidopaterno)
print("Apellido materno: " + apellidomaterno)
print("Edad: " + str(edad) + "años")
print("Peso: " + str(peso))
print("Estatura: " + str(estatura))
print("")
print("Su IMC es: " + str(IMC))

#VALIDACIONES, LA FUENTE DE LOS RESULTADOS ES DEL GOBIERNO DE MEXICO CON LA SECRETARIA DE SALUD (LIGA PROPORCIONADA POR UCAMP)

if IMC >=0 and IMC <=15.99 : #se utiliza para determinar en qué categoria cae el resultado de IMC
    print("Usted cuenta con: delgadez severa")
elif IMC >=16.00 and IMC <=16.99 :
    print("Usted cuenta con: delgadez moderada")
elif IMC >=17.00 and IMC <=18.49 :
    print("Usted cuenta con: delgadez leve")
elif IMC >=18.50 and IMC <=24.99 :
    print("Usted cuenta con: peso normal")
elif IMC >=25.00 and IMC <=29.99 :
    print("Usted cuenta con: sobrepeso")
elif IMC >=30.00 and IMC <=34.99 :
    print("Usted cuenta con: obesidad leve")
elif IMC >=35.00 and IMC <=39.00 :
    print("Usted cuenta con: obesidad media")
elif IMC >=40.00 :
    print("Usted cuenta con: obesidad morbida")







