# Controle de Temperatura de Forno
# Um forno industrial inicia com temperatura informada pelo usuário. -
# A cada ciclo: -
# Se temperatura < 800 → aumenta 50 graus -
# Se temperatura ≥ 800 e < 1000 → aumenta 20 graus -
# Se temperatura ≥ 1000 → mantém constante - 
# O sistema deve repetir até:
# Atingir 1000 graus
# Exibir:
# Quantos ciclos foram necessários
# Temperatura final

contador = 0

temp = float(input("Digite a temperatura do forno: "))

while True:
    contador += 1
    if temp < 800:
        temp += 50
    elif temp >= 800 and temp < 1000:
        temp += 20
    else:
        temp = temp

    if temp >= 1000:
        print ("Foram necessários: " , contador , " ciclos para a temperatura ultrapassar os 1000 graus.")
        print ("A temperatura final é: " , temp)
        break
    