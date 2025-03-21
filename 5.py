numeros = []

while True:
    num = input("insira um um numero:  ")

    num= int(num)

    if numeros and num == numeros [-1]:
        print("numero repetido ao ultimo, voce encerrou o programa.")
        break
    

    numeros.append(num)
    print(f"numeros inseridos: {numeros}")
    len(numeros)
    print(len)