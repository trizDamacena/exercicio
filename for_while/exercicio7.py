frase = input("Digite uma frase: ").split()
newfrase = ''
c = ''
a = 0
e = 0
i = 0
o = 0
u = 0
for palavra in frase:
    newfrase += palavra
newfrase = str.lower(newfrase)

char = list(newfrase)
print(c)
for c in char:
    if c == 'a':
        a += 1
    elif c == 'e':
        e += 1
    elif c == 'i':
        i += 1
    elif c == 'o':
        o += 1
    elif c == 'u':
        u += 1
print(f'A = {a}\nE = {e}\nI = {i}\nO = {o}\nU = {u}\n')