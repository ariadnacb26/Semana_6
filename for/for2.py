#Leer un numero ingresado por el usuario 
#Mostrar la letra a por cada numero del 1 al numero 
#Ingresado por el usuario ejemplo, numero: 3
#a
#aa
#aaa

def mostrarletra(numero):
    for i in range(1, numero+1):
        print(f"a" * i)
            
def main():
    num = int(input("Ingrese un numero: "))
    mostrarletra(num)            
    
    main()