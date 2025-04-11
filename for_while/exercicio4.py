v1 = int(input("Digite o primeiro numero: "))
v2 = int(input("Digite o segundo número: "))
primo = 0
lprimo = []
lnprimo = []

for num in range(v1+1, v2):
    for i in range(1, num+1):
        if num > 1 and num % i == 0:
            primo += 1
    if primo < 3:
        lprimo.append(num)
    else:
        lnprimo.append(num)
    primo -= primo

print(f'Os números primos são {lprimo}')
print(f'Os números que não são primos: {lnprimo}')