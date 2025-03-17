peso = float(input('Digite seu peso (kl): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('''    Seu peso é de {}
    Sua altura é de {}
    Você esta Abaixo do peso!''' .format(peso, altura))

elif imc > 18.5 and imc < 24.9:
    print('''    Seu peso é de {} kilos
    Sua altura é de {} metros
    Seu peso esta normal!''' .format(peso, altura))

elif imc > 24.9 and imc < 29.9:
    print('''    Seu peso é de {} kilos.
    Sua altura é de {} metros.
    Você está Sobrepeso!''' .format(peso, altura))

elif imc > 29.9 and imc < 34.9:
    print('''    Seu peso é de {} kilos.
    Sua altura é de {} metros.
    Você está com Obesidade grau I''' .format(peso, altura))

elif imc > 35 and imc < 39.9:
    print('''    Seu peso é de {} kilos.
    Sua altura é de {} metros.
    Você tem Obesidade grau II''')

else:
    print('Você tem obesidade nivel III!')

input()
