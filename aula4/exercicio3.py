"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,45 para viagens mais longas.
"""

km=float(input("Quantos km quer percorrer? "))
if km <= 200:
    passagem = km * 0.50
    print(f' O valor a pagar por percorrer a distância de {km} é R$ {passagem}')
else:
    passagem = km * 0.45
    print(f' O valor a pagar por percorrer a distância de {km} é R$ {passagem}')

