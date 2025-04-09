numeros = input().split()
par = []
impar =[]
for numero in numeros:
    numero = int(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Números pares: {par}")
print(f"Números impares: {impar}")