# Máquina com Desgaste Acumulativo
# Uma máquina começa com desgaste 0.
# A cada ciclo:
# Desgaste aumenta 7 unidades
# Se operar acima de 70 ciclos, desgaste aumenta 10 por ciclo
# Se desgaste ≥ 500 → máquina quebra
# Simular até quebrar.
# Exibir:
# Quantos ciclos durou
# Desgaste final

maq = 0
contador = 0

while True:
    maq += 7
    contador += 1

    if contador >= 70:
        maq += 10

    if maq >= 500:
        print ("Máquina quebrou!")
        print ("A máquina durou " , contador , " ciclos.")
        print ("O desgaste final da máquina é: " , maq)
        break