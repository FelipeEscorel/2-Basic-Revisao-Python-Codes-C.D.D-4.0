opcao = 1
while opcao != 2:
    num = float(input("Digite um número qualquer: "))
    if num % 2 == 0 and num < 0:
        print(f"\n{num} é par e negativo")
    elif num % 2 == 0 and num >= 0:
        print(f"\n{num} é par e positivo")
    elif num % 2 != 0 and num < 0:
        print(f"\n{num} é ímpar e negativo")
    elif num % 2 != 0 and num >= 0:
        print(f"\n{num} é ímpar e positivo")
    opcao = int(input("\nDeseja continuar? Digite 1 para sim e 2 para não: "))
