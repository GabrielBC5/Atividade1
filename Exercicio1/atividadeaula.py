aluno = {"Thiago", "DiegoBrothers", "Gabriel"}
numero = {1, 2, 3}
cidade = {"Goiania", "Tangara", "Colider"}
print (aluno, numero, cidade)

alunos = ["Ana", "Bruno"]
professorA = alunos
professorB = alunos
professorA.append("Carlos")
print("Professor A", professorA)
print("Professor B", professorB)

#tanto alunos, quanto professorA e professorB apontam para o mesmo objeto na memoria.
#ambos vem o mesmo resultado porque ambos estão atrelados a alunos
#existe apenas uma lista, a lista alunos
#uma maneira de resolver seria usando {}

alunos = {"Ana", "Bruno"}
professorA = alunos.copy()
professorB = alunos.copy()
professorA.add("Carlos")
print("Professor A", professorA)
print("Professor B", professorB)

#.copy() cria um novo objeto na memória com os mesmos elementos
#O problema do codigo original é que ambos professorA e professorB estão puxando a informação
#da mesma propriedade "alunos", ou seja, mesmo que professorA mude algo em alunos o professorB
#também vai receber a mudança.
#depois da correção existem duas listas
#a função usada para resolver o problema foi a .copy