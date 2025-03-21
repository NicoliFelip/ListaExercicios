votos_candidatos = [0] * 4  
votos_nulos = 0
votos_brancos = 0
total_votos = 0

while True:

        voto = int(input("Digite seu voto (1-4 candidato, 5-nulo, 6-branco, 0-encerrar): "))
        if voto == 0:
            break
        elif 1 <= voto <= 4:
            votos_candidatos[voto - 1] += 1
        elif voto == 5:
            votos_nulos += 1
        elif voto == 6:
            votos_brancos += 1
        else:
            print("Voto inválido.")
        total_votos +=1
    

print("\nResultados da votação:")
for i in range(4):
    print(f"Candidato {i + 1}: {votos_candidatos[i]} votos")

print(f"Votos nulos: {votos_nulos}")
print(f"Votos brancos: {votos_brancos}")

if total_votos > 0:
    percentual_nulos = (votos_nulos / total_votos) * 100
    percentual_brancos = (votos_brancos / total_votos) * 100
    print(f"\nPercentual de votos nulos: {percentual_nulos:.2f}%")
    print(f"Percentual de votos brancos: {percentual_brancos:.2f}%")
else:
  print("\nNenhum voto computado.")