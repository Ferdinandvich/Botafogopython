alunos = []

for i in range (4):
    nomeAluno = input("Digite o nome : ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
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

nomeAluno.sort
print(alunos)