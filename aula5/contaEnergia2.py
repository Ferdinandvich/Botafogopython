"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica
Pergunte a quantidade de KW consumida e o tipo de instalação: R para residências, I para 
indústria e C para comércio. Calcule o preço a pagar de acordo com a tabela a seguir.
"""

consumo = int(input("Qual o seu consumo? "))
tipo = input("Sua instalação é residencial \n I - Industrial, \n C - Comercial \n R - Residencial ? ")

if tipo == "R":
    if consumo <= 500:
       custo = 0.40
    else:
       custo = 0.65

elif tipo == "C":
    if consumo <= 1000:
       custo = 0.55
    else:
       custo = 0.60

elif  tipo == "I":
    if consumo <= 5000:
       custo = 0.70
    else:
       custo = 0.80
else:
    precopagar = 0
    print("Erro ! Tipo de Instalação desconhecido")
total = consumo * custo
print(f'O valor a pagar R$ {total}')