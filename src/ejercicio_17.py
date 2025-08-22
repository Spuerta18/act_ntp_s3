# Pedir un número al usuario
numero = int(input("Ingresa un número entero de 2 cifras positivo: "))

# Convertir el número a cadena para recorrer cada dígito
suma = 0
for digito in str(numero):
    suma += int(digito)

print("La suma de los dígitos es:", suma)
