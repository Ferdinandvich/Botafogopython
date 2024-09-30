"""
Cria função para input - Pergunta nomes e notas e publica no final.
"""

def calcularMedia(n1, n2):
    media = (n1 + n2)/2
    return media 

def imprimirAlunos(alunos): 
    for aluno in alunos:
        print(aluno["nome"], " (Media: ", aluno["media"], "-",aluno["resultado"]," )")

def lerValor(mensagem):
    valorLido = input(mensagem)
    return valorLido

resposta = int(input("Quantos alunos para calcular? "))

i = 0
alunos = []

while i < resposta: 

    nomeAluno = lerValor("Digite seu nome : ")
    nota1 = float(lerValor("Digite a primeira nota : "))
    nota2 = float(lerValor("Digite a segunda nota : "))
    

    media = calcularMedia(nota1, nota2)

    resultado = "Aprovado" if media >= 6.5 else "Reprovado"

    alunos.append(
        {
            "nome": nomeAluno,
            "nota1": nota1,
            "nota2": nota2,
            "media": media,
            "resultado": resultado

        }
    
    )

    i = i + 1

imprimirAlunos(alunos)