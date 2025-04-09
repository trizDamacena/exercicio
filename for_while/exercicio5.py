senha = "1234"
contador = 0
veri = 0
while 3 > contador:
     user = input("Digite a senha: ")
     if user == senha:
         contador +=3
         print("Entrou")
         veri = 1
     else:
        contador += 1
if veri == 0:
    print("Acesso Bloqueado")