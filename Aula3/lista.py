alunos = ["Simone", "Vanessa","Fernando", "Ricardo"] # lista
             #0          1         2           3

#turma = {"Simone", "Vanessa","Fernando", "Ricardo"} # set
#print (turma)
print (alunos [2])
alunos[2] = "Fernando Telles"
print(alunos)

# adicionar valor em lista
alunos.extend(["gustavo"])
print(alunos)
# adicionar um registro em lista
alunos.append("aurelio")
print(alunos)

alunos.insert(0,"maria eduarda")
print(alunos)

alunos.remove("Vanessa")
print(alunos)
# R E M O V E no final da lista
alunos.pop()
print(alunos)
alunos.pop() # elimina o último da lista
print(alunos)
# Apagar o conteúdo de uma lista
# alunos.clear()
print(alunos)

alunos.sort()
print(alunos)