#Solicitar al usuario un numero entero positivo 
#Usa un bucle para que vaya de 1-10 
#En cada iteracion, multiplicar el numero ingresado 
#Muestra el resultado en cada paso en pantalla

numero = int(input("Ingresa un número: "))

while numero <= 0:
    print("El número debe ser mayor que 0")
    numero = int(input("Ingresa un numero: "))


for i in range(1, 11):
 
    resultado = numero * i
    
    print(f"{numero} * {i} = {resultado}")