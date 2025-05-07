def eh_primo(n):
    primo = 0
    for i in range(1,n+1):
        if n % i == 0:
            primo += 1
    if primo == 2:
        return True
    else:
        return False
n = int(input("Digite um número: "))

print(eh_primo(n))

