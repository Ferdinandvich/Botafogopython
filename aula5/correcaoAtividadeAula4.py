num1 = int(input("Digite o primeiro número. "))
num2 = int(input("Digite o segundo número. "))
operacao = input("Deseja realizar soma ou o que? ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print("operação inválida")
    resultado = 0
print("Resultado :", resultado)