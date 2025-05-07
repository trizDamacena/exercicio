def calcular_IMC():
    IMC = peso/(altura**2)
    return IMC
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

print(f"O IMC é {calcular_IMC():.2f}")