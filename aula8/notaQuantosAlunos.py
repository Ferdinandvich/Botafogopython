"""
Pergunta de quantos alunos quer calcular a média.
"""
resposta = int(input("Quantos alunos para calcular? "))
for i in range (resposta): #aqui, resposta limita a contagem do i, que é um contador
    nomeAluno = input("Digite seu nome : ")
    nota1 = float(input("Digite a primeira nota : "))
    nota2 = float(input("Digite a segunda nota : "))
    media = (nota1 + nota2)/2
 


