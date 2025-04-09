import random
opcao = ["cara", "coroa"]
contador = 0


while contador < 3:
    lado = random.choice(opcao)
    print(lado)
    if lado == "cara":
        contador +=1
    elif contador > 0:
        contador -= contador
