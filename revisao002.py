num = float(input("Digite um número qualquer: "))

if num % 2 == 0 and num < 0:
    print(f"{num} é par e negativo")
elif num % 2 == 0 and num >= 0:
    print(f"{num} é par e positivo")
elif num % 2 != 0 and num < 0:
    print(f"{num} é ímpar e negativo")
elif num % 2 != 0 and num >= 0:
    print(f"{num} é ímpar e positivo")
