suma = 0

while True:
    numero = float(input("Ingresa un número: "))
    suma += numero  
    if suma > 100:  
        break

print(f"La suma total es: {suma}")