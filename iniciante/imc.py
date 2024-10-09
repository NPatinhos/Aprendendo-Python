nome = "Fernanda"
altura = 1.74
peso = 74
imc = peso / (altura ** 2)

print(nome, "tem", altura, "m de altura, pesa", peso, "kg e seu IMC é", round(imc, 2 ))

linha1 = f"{nome} tem {altura:.2f}m de altura e {peso}kg"
linha2 = f"seu IMC é {imc:.3f}"

print(linha1, "\n", linha2)
#print(linha2) 