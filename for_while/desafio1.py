nGeracoes = int(input("Quantas gerações de coelhos deseja calcular: "))
nCoelhos = int(input("Digite o número de coelhos: "))
tReproducao = int(input("Qual a taxa de reprodução: "))
tMortalidade = int(input("Qual a taxa de mortalidade: "))
coelhosNovos = 0
for geracao in range(nGeracoes):
    tReproducao = (nCoelhos *tReproducao)/100
    tMortalidade = (nCoelhos * tReproducao)/100
    nCoelhos += tReproducao
    nCoelhos -= tMortalidade
    coelhosNovos += nCoelhos
    print(tReproducao, tMortalidade)
print(coelhosNovos)