# texto_variado= "palabra 123 +"
# print(type(texto_variado))

# # # Podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito
# # print("""
# # Funcionamiento de \
# # programa: (opciones)
# #     -1 Para acceder a opciones
# #         -2 para salir
# # """)

# # Susbscripting e indexado

# texto = "Python"

# # print(texto[0])
# # print(texto[5])
# # print(texto[-1])
# # print(texto[-6])

# # print(texto[6]) #error no podemos acceder a 1 posicion que no exite, fuera de rango
# # print(texto[-7]) #error, lo mismo

# letra = texto[0]
# print(letra)

# # texto[0] = "p" # Error, no podemos modificar una cadena

# letra = "p" 
# print(letra)

# texto_compuesto = letra + texto[1] #concatenación
# print(texto_compuesto)


#########################################################

# Slicing o Substringing # seleccionar un rango de indices
# texto = "Python"
# print(texto[0:3]) # el indice del final no se toma en cuenta, el 3, hasta uno previo ,seimrpime 0,1 y 2, 3 no

# print(texto[0:-3]) # misma impresion, n-1, o-2, h-3
# print(texto[0:-2]) 
# print(texto[2:]) # no especificamos el ultimo punto
# print(texto[:3]) # desde el principio de la cadena hasta 3


# print(texto[-3::-1])

# print(texto[::-1]) #-1 se impreme al reves
# print(texto[1:50])
# print(texto[2:2]) # no se imprime nada porque el ultimo de los elementos no se toma en cuenta
#############################################################################################################

# Cadenas y formatos
# texto= "Hola mundo! Buenastardes"
# print(texto.lower()) # poner todo en minusculas, homolgar una gran cantidad de variables
# print(texto.upper()) # poner todo en mayusculas
# print(texto.capitalize()) # la primera letra de toda la cadena en mayusculas
# print(texto.title()) # que la inicial de cada palabra sea mayuscula
# print(texto.swapcase()) # intercambias mayusculas por minusculas

# texto= texto.upper()
# print(texto)

# 



