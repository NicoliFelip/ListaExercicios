num_secreto= 8
tentativa= int(input("tentativa de adivinhar o numero secreto de 1 a 10:  "))
while tentativa != num_secreto:
    tentativa= int(input("tentativa de adivinhar o numero secreto de 1 a 10"))

    print(f"numero correto! resposta {num_secreto}")