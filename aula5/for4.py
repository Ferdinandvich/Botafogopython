# solicito o usuário para digitar um número
numero = int(input("Digite um número"))
# inicializo o número
for index in range (10):
    aux = index * numero
    print(index, " x", numero, " =", aux)