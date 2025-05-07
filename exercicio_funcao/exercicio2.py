def maior_n(n):
    lista = []
    for i in range(1,n+1):
        lista.append(int(input("Digite um número: ")))
    maior = max(lista)
    return maior
n = int(input("Digite o total de números: "))

print(f"O maior número é: {maior_n(n)}")