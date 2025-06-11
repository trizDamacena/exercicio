alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z"]
crip = ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c","D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "B", "C"]
textoCripto = []

with open("./Lista_ManipulacaoArquivos/criptografado.txt", "r", encoding='utf-8') as f:
    conteudo = f.read()
    for letra in conteudo:
        with open("./Lista_ManipulacaoArquivos/descriptografado.txt", "a", encoding='utf-8') as f:
            if letra in alfabeto:
                posicao = int(crip.index(letra))
                new_letra = str(alfabeto[posicao])
                
            else:
                new_letra = letra
            f.write(new_letra)

