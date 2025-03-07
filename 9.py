numeros= int(input("insira numeros pares, e um numero impar para interromper o programa :  "))
par= numeros %2 == 0
numeros+=1
while numeros==par:

    pares= int(input("insira numeros pares, e um numero impar para interromper o programa :  "))
    contador= numeros +pares
    print(f"voce digitou {contador} numeros pares" )
    break