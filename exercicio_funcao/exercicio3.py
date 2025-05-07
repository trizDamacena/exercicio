def converter_celsius_para_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    print(f"A temperatura é {fahrenheit:.2f}")
c = float(input("Digite a temperatura em C°: "))

converter_celsius_para_fahrenheit(c)