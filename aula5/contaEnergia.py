"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica
Pergunte a quantidade de KW consumida e o tipo de instalação: R para residências, I para 
indústria e C para comércio. Calcule o preço a pagar de acordo com a tabela a seguir.
"""

consumo = int(input("Qual o seu consumo? "))
tipo = input("Sua instalação é residencial (r), indústria (i) ou comércio (c)? ")

if tipo == "r" and consumo <= 500:
    print(consumo * 0.40)
if tipo == "r" and consumo > 500:
    print(consumo * 0.65)

if tipo == "c" and consumo <= 1000:
    print(consumo * 0.55)
if tipo == "c" and consumo > 1000:
    print(consumo * 0.60)

if tipo == "i" and consumo <= 5000:
    print(consumo * 0.70)
if tipo == "i" and consumo > 5000:
    print(consumo * 0.80)