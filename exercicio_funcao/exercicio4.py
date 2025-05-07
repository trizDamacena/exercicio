def calcular_troco(valor_compra, valor_pago):
    if valor_pago < valor_compra:
        print("Valor insuficiente.")
    else:
        troco = valor_pago - valor_compra
        print(f"O valor do troco é {troco}")
valor_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor dado pelo cliente: "))

calcular_troco(valor_compra,valor_pago)