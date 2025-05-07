def contar_vogais(texto):
    texto = texto.replace(" ", "")

    vogais = texto.count("a")
    vogais += texto.count("e")
    vogais += texto.count("i")
    vogais += texto.count("o")
    vogais += texto.count("u")
    print(vogais)
texto = input("Digite uma palavra: ")

contar_vogais(texto)