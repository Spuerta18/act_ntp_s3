edad = 0
mayor = -1  # valor inicial bajo para comparar

while edad != -1:
    edad = int(input("Ingresa una edad (-1 para terminar): "))
    if edad != -1 and edad > mayor:
        mayor = edad

if mayor != -1:
    print("La edad mayor ingresada es:", mayor)
else:
    print("No se ingresaron edades válidas.")
