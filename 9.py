# Implemente um sistema onde o usuário insere o código e a quantidade dos produtos
# desejados. O programa deve calcular o valor total e permitir que o usuário finalize o
# pedido digitando 0.

banana="1"
laranja="2"
tomate="3"

codigo = "a"

while True:
    codigo = input("Insira o código do produto (ou 0 para finalizar): ")

    if codigo != "0":
        if codigo != banana or codigo != laranja or codigo != tomate:
            print("Codigo errado")
        else:
            quantidade= int(input("quantidade:  "))
            if codigo == banana:
                calculoBanana= quantidade * 2,50
                print(calculoBanana)
            elif codigo == laranja:
                calculoLaranja= quantidade * 3,50
                print(calculoLaranja)
            elif codigo == tomate:
                calculoTomate= quantidade * 4,20
                print(calculoTomate)
    else:
        break
    
 
 