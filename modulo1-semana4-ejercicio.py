# Hacer un formluario simple de registro de usuarios

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: ")) # En calculos de edad usar siempre la transformación a entero, Int= a entero
correo = input("Introduce el correo electronico: ")
telefono = input("Introduce tu telefono: ") # Se deja sin int, porque si empieza en 0 a la izquierda no se toma en cuenta


print("Nombre: " + nombre)
print("Apellido " + apellido)
print("Tengo " + str(edad))
print("Correo: " + correo)
print("Teléfono: " + telefono)
