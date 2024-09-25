nome = input("Digite seu nome : ")
nota1 = float(input("Digite a primeira nota : "))
nota2 = float(input("Digite a segunda nota : "))
media = (nota1 + nota2)/2

if(media >= 6.5):
    print(media, nome, "Aprovado!" ) 
else: 
    print(media, nome, "Reprovado!" ) 

