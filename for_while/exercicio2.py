senha = "1234"
vezes = 0
while True:
    senhaUser = input(f"{vezes}) Digite a senha: ")
    vezes += 1
    if senhaUser == senha:
        print("Senha correta")
        break

