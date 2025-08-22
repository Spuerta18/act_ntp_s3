contador = 0
palabra = ""

while palabra != "fin":
    palabra = input("Escribe una palabra (o 'fin' para terminar): ")
    if palabra != "fin":
        contador += 1

print("Se leyeron", contador, "palabras.")
