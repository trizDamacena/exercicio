import random
import re
from operator import index

palavras = ['python', 'quarta', 'salgado', 'brigadeiro']
escolha = random.choice(palavras)
espaco = []
b =1
chances = 1

len(escolha)
print(escolha)
for i in range(len(escolha)):
    espaco.append('_')

while chances <=5:
    while True:
        print(espaco)
        char = input('Digite uma letra: ')
        if re.findall(char, escolha):
            print(f'A leta {char} aparece {escolha.count(char)}')
            local = int(input('Onde deseja colocar a letra: '))
            espaco[local] = char

        else:
            print(f'Vezes: {chances}')
            break

    chances += 1
