"""
Pergunta nomes e notas e publica no final.
"""
resposta = int(input("Quantos alunos para calcular? "))

i = 0
alunos = []

while i < resposta: 

    nomeAluno = input("Digite seu nome : ")
    nota1 = float(input("Digite a primeira nota : "))
    nota2 = float(input("Digite a segunda nota : "))
    media = (nota1 + nota2)/2
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

print(alunos)

i = i + 1

# if(media >= 6.5):
   # print(f"{media} - Aprovado!" ) 
#else: 
   # print(f"{media} - Reprovado!" )

    

