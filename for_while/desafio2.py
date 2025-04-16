import random
import re
from operator import index

palavras = ['python', 'quarta', 'salgado', 'brigadeiro']
escolha = random.choice(palavras)
espaco = []
letrasCertas = []
letrasErradas = []
palavraUsuario = ""


verificador = 0
tamanho = 0
chances = 1

len(escolha)

for i in range( len(escolha)):
    espaco.append('_')
    tamanho = i
tamanho += 1

while chances <=6:
    while True:
        print(espaco)
        if len(letrasErradas) != 0:
            print(f"Letras erradas que já foram:{letrasErradas}")

        char = input('Digite uma letra: ')

        for i in letrasErradas:
            if char == i:
                char = input(f"A letra {char} ja foi, digite outra: ")
        for i in letrasCertas:
            if char == i:
                char = input(f"A letra {char} ja foi, digite outra: ")



        if re.findall(char, escolha):
            letrasCertas.append(char)
            print(f'\nA letra {char} aparece {escolha.count(char)}')
            if escolha.count(char) >= 2:
                local = int(input("Onde deseja por a primeira letra: "))
                espaco[local] = char
                verificador += 1
                local = int(input("Onde deseja colocar a segunda letra: "))
                espaco[local] = char
                verificador += 1
            else:
                local = int(input('Onde deseja colocar a letra: '))
                espaco[local] = char
                verificador += 1


            if verificador >= tamanho:
                conferirPalavra = palavraUsuario.join(espaco)
                if conferirPalavra == escolha:
                    verificador = 20

                else:
                    chances +=1
                    print(f'Algum caracter está errado!\nVocê já teve: {chances}')
        if verificador == 20:
            chances += 20
            print("\nParabéns! Você ganhou")
            print(f"A palavra era: {escolha}")
            break
        else:
            letrasErradas.append(char)
            print(f'Vezes: {chances}')
            break

if chances < 20:
    print("\nVocê perdeu")
    print(f"A palavra era: {escolha}")

