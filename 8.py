numeros=int(input("insira numeros para que seja encontrado o maior deles. Para parar, digite '0'. :  "))
maior= 0
while numeros != 0 :
    if  numeros >  maior: 
        maior= numeros
    numeros=int(input("insira numeros para que seja encontrado o maior deles. Para parar, digite '0'. :  "))
print(f" contagem encerrada.  {maior}")




