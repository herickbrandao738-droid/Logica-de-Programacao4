# Balanceamento Dinâmico de Linha de Produção
# Uma linha tem 5 estações.
# Cada estação:
# Recebe peças
# Processa no máximo X por ciclo
# Pode quebrar se operar acima de 90% da capacidade por 5 ciclos seguidos
# Regras:
# Peças não processadas acumulam
# Se uma estação quebra:
# Toda a linha para
# Produção continua até:
# Meta diária atingida
# Ou falha estrutural
# Exibir:
# Produção total
# Estação que falhou (se houver)
# Ciclos executados

pcs = 0
ciclo = 0
meta = 0

E1 = 0
E2 = 0
E3 = 0
E4 = 0
E5 = 0
totalP = 0

pecasPassarE1 = 0
pecasPassarE2 = 0
pecasPassarE3 = 0
pecasPassarE4 = 0
pecasPassarE5 = 0

print("----- Balanceamento Dinâmico de Linha de Produção -----")
pcs = int(input("Digite quantas peças irão entrar por ciclo: "))
meta = int(input("Digite qual é a meta de peças do dia de hoje: "))

limiteE1 = int(input("Digite o número máximo de peças para a estação 1: "))
limiteE2 = int(input("Digite o número máximo de peças para a estação 2: "))
limiteE3 = int(input("Digite o número máximo de peças para a estação 3: "))
limiteE4 = int(input("Digite o número máximo de peças para a estação 4: "))
limiteE5 = int(input("Digite o número máximo de peças para a estação 5: "))

while True:
    ciclo += 1

    # --- ESTAÇÃO 1 ---
    cargaE1 = E1 + pcs
    if cargaE1 > limiteE1:
        E1 = cargaE1 - limiteE1
        pecasPassarE1 = limiteE1
    else:
        E1 = 0
        pecasPassarE1 = cargaE1

    # --- ESTAÇÃO 2 ---
    cargaE2 = E2 + pecasPassarE1
    if cargaE2 > limiteE2:
        E2 = cargaE2 - limiteE2
        pecasPassarE2 = limiteE2
    else:
        E2 = 0
        pecasPassarE2 = cargaE2

    # --- ESTAÇÃO 3 ---
    cargaE3 = E3 + pecasPassarE2
    if cargaE3 > limiteE3:
        E3 = cargaE3 - limiteE3
        pecasPassarE3 = limiteE3
    else:
        E3 = 0
        pecasPassarE3 = cargaE3

    # --- ESTAÇÃO 4 ---
    cargaE4 = E4 + pecasPassarE3
    if cargaE4 > limiteE4:
        E4 = cargaE4 - limiteE4
        pecasPassarE4 = limiteE4
    else:
        E4 = 0
        pecasPassarE4 = cargaE4

    # --- ESTAÇÃO 5 ---
    cargaE5 = E5 + pecasPassarE5_anterior if 'pecasPassarE5_anterior' in locals() else E5 + pecasPassarE4
    cargaE5 = E5 + pecasPassarE4
    if cargaE5 > limiteE5:
        E5 = cargaE5 - limiteE5
        pecasPassarE5 = limiteE5
    else:
        E5 = 0
        pecasPassarE5 = cargaE5

    # Atualiza a produção acumulada que finalizou na E5
    totalP += pecasPassarE5

    # --- VERIFICAÇÃO DE SOBRECARGA (90% DO LIMITE) ---
    if E1 > limiteE1 * 0.9 or E2 > limiteE2 * 0.9 or E3 > limiteE3 * 0.9 or E4 > limiteE4 * 0.9 or E5 > limiteE5 * 0.9:
        print("\n[ALERTA DE SOBRECARGA] Uma das estações ultrapassou 90% da capacidade acumulada!")

    # Condição de parada principal
    if totalP >= meta:
        break

# --- CÁLCULO DE EFICIÊNCIA ---
eficiencia = (totalP / meta) * 100

# --- IDENTIFICAÇÃO DO GARGALO (MAIOR FILA) ---
gargalo = "Estação 1"
maior_fila = E1

if E2 > maior_fila:
    gargalo = "Estação 2"
    maior_fila = E2
if E3 > maior_fila:
    gargalo = "Estação 3"
    maior_fila = E3
if E4 > maior_fila:
    gargalo = "Estação 4"
    maior_fila = E4
if E5 > maior_fila:
    gargalo = "Estação 5"
    maior_fila = E5

# --- EXIBIÇÃO DOS RESULTADOS ---
print("\n================ RESULTADOS FINAIS ================")
print(f"Total de ciclos necessários: {ciclo}")
print(f"Produção total finalizada: {totalP} peças")
print(f"Percentual de meta atingido: {eficiencia:.1f}%")
print(f"Principal gargalo da linha: {gargalo} (com {maior_fila} peças paradas)")
print("---------------------------------------------------")
print(f"Saldo na Fila E1: {E1} peças")
print(f"Saldo na Fila E2: {E2} peças")
print(f"Saldo na Fila E3: {E3} peças")
print(f"Saldo na Fila E4: {E4} peças")
print(f"Saldo na Fila E5: {E5} peças")
print("===================================================")