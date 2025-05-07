def contagem_regressiva(n):
    for i in range(n +1):
        numero = n - i
        if numero == 1:
            print(f"Contagem: {numero}")
            print("FIM")
            break
        else:
            print(f"Contagem: {numero}")

n = int(input("Digite o tempo: "))
contagem_regressiva(n)