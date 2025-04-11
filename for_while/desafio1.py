nGeracoes = int(input("Quantas gerações de coelhos deseja calcular: "))
nCoelhos = int(input("Digite o número de coelhos: "))
tReproducao = int(input("Qual a taxa de reprodução: "))
tMortalidade = int(input("Qual a taxa de mortalidade: "))
coelhosNovos = 0

for geracao in range(1, nGeracoes+1):
    R = tReproducao = (nCoelhos *tReproducao)//100
    M =tMortalidade = ((nCoelhos + R) * tMortalidade)//100
    nCoelhos += R
    nCoelhos -= M
    coelhosNovos += nCoelhos
print(f'\nEm {nGeracoes} era ter {coelhosNovos} coelhos.')
