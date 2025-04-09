numeros = input().split()
multiplos = 0

for numero in numeros:
    numero = int(numero)

    if numero % 3 == 0:
        multiplos +=1
print(f"O total de numeros multiplos de 3 é: {multiplos}")