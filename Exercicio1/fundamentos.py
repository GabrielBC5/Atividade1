#forma errada de listar
#varias variaveis, cada aluno é uma variavel
nome1 = "Arthur"
nome2 = "Pedro"
nome3 = "Vinicius"
nome4 = "Augusto"
nome5 = "Diego"
nome6 = "Jorge"
nome7 = "Maria"
nome8 = "Daniel"
nome9 = "Miguel"
nome10 = "Donatelo"

print(nome1)
print(nome2)
print(nome3)
print(nome4)
print(nome5)
print(nome6)
print(nome7)
print(nome8)
print(nome9)
print(nome10)

#forma correta
aluno = {"Arthur", "Pedro", "Vinicius", "Augusto", "Diego", "Jorge", "Maria", "Daniel", "Miguel", "Donatelo"}
print(aluno)

alunos = {"Miguel","Raphael","Michelangelo","Donatelo","Leonardo"}

buscar = "Miguel"
if buscar in alunos:
    print("Nome encontrado")
else:
    print("Não encontrado")
        
for numero, aluno in enumerate(alunos, start=1):
    print(numero, aluno)

    alunos = ["Igor","Bruna","João"]
for aluno in alunos:
    print(aluno) 
    #ele precisa estar dessa forma para estar dentro do laço