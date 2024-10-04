"""
Quantas notas de 50, 10 e 1 para um valor solicitado no caixa eletrônico.

"""
resposta = "S"

while resposta == "S":
    saque = int(input ("Quanto quer sacar ? "))
    
    n50 = (saque // 50)
    n10 = (saque % 50) // 10
    n1 = (saque % 50) % 10

    print("Notas de cinquenta :" , n50)
    print("Notas de dez :", n10)
    print("Moedas de um :", n1)

    resposta = input("Deseja fazer outro saque (S/N)? ")

