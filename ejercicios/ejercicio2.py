numero = int(input("Ingresa un número positivo: "))
while numero < 0:
    print("Por favor, ingresa un número mayor o igual a 0.")
    numero = int(input("Ingresa un número positivo: "))


contador = 0

while contador <= numero:
   
    if contador % 2 == 0:
       
        print(contador)
    
 
    contador += 1