peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso / (altura * altura)
print(f"Seu IMC é de {IMC:.1f}")

if IMC <= 18.5:
    print("Você está abaixo do peso.")
elif 18.6 <= IMC <= 24.9:
    print("Você está no peso ideal!")
elif 25.0 <= IMC <= 29.9:
    print("Você está levemente acima do peso.")
elif 30.0 <= IMC <= 34.9:
    print("Você tem obesidade de grau I")
elif 35.0 <= IMC <= 39.9:
    print("Você tem obesidade de grau II (Severa)")
elif IMC >= 40.0:
    print("Você tem obesidade de grau III (Mórbida)")
