numero = input("Digite uma sequencia de numero(Ex: 1 2 3 4 5): ").split()
soma = 0

for n in numero:
    n = int(n)
    soma += n
media = soma / len(numero)
print(f"A MÉDIA É: {media}\nNúmeros maiores:")

for n in numero:
    n = int(n)
    if n >= media:
        print(n)