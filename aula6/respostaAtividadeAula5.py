# tratamento de exceção
"""
Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até
que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados,
assim como a soma e a média aritmética
"""

import math
soma = 0 
quantidade = 0
#exemplo = 10
# soma = 0 ; quantidade = 0 ; exemplo = 10
while True:
    numero = int(input("Digite um número : "))
    if numero == 0:
        break
    #quantidade = quantidade + 1
    quantidade += 1
    # soma = soma + numero
    soma += numero
print("A soma é : " , soma)
print("Total de números digitados : " , quantidade)
print("Média Aritmética : " , math.ceil(soma/quantidade))
# print("Exemplo : " , exemplo)

