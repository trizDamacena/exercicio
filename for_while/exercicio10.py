numeros = input("Digite uma sequencia de numero(Ex: 1 2 3 4 5): ").split()
numero = 0
for n in numeros:
    n = int(n)
    if n > numero:
        numero = n
print(f"{n} é o maior")