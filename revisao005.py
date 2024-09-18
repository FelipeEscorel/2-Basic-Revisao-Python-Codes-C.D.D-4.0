opcao = 1

while opcao != 2:

    A = int(input("Digite um valor inteiro: "))
    B = int(input("Digite outro valor inteiro: "))
    if A == B:
        C = A + B
        print(f"Os valores de A({A}) e B({B}) são iguais. Logo a soma dos dois é {C}.")
    else:
        C = A * B
        print(f"Os valores de A({A}) e B({B}) são diferentes. Logo a multiplicaçao dos dois é {C}.")
    opcao = int(input("Deseja continuar? 1 para sim e 2 para não: "))
