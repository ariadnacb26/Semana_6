import random
numero_secreto = random.randint(1, 10)

intento = int(input("Adivina el número (entre 1 y 10): "))

while intento != numero_secreto:
    if intento < numero_secreto:
        print("Intenta con un número mayor")
    else:
        print("Intenta con un número menor")
   
    intento = int(input("Intenta nuevamente: "))

print("¡Felicidades! Adivinaste el número")