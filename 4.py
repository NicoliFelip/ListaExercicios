maior_numero= None
while True:
    numero= float(input("insira um numero positivo para dar continuidade, e um negativo para encerrar  programa:  "))

    if numero <0:
        break

    if maior_numero is None or numero > maior_numero:
        maior_numero= numero

        if maior_numero is not None:
            print(f"o maior numero foi : {maior_numero}")
        else:
            print("nenhum numero foi informado.")