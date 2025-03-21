# Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. 
# Caso a média seja igual ou superior a 7, apresente a mensagem "APROVADO", caso contrário, armazene a nota da prova final e recalcular a média. 
# Caso a nova média seja igual superior a 5, apresente a mensagem "APROVADO", caso contrário, apresente a mensagem "REPROVADO"

notas = []
contador = 1

aluno = input('Digite o nome do Aluno: ')
disciplina = input('Digite o nome da matéria: ')

while contador < 5:
    notas.append(float(input(f'Informe a nota do {contador}º bimestre do aluno {aluno}: ')))
    contador += 1

media = sum(notas) / len(notas) # Função len indica quantos elementos tem dentro da lista
print(f'A média final de {aluno} foi {media}')
if media >= 7:
    print(f'O aluno {aluno} foi APROVADO! Parabéns!!!')
else:
    print(f'O aluno {aluno} ficou de RECUPERAÇÃO! Estudo um pouco mais. Boa sorte!!!')
    notas.append(float(input(f'Informe a nota da prova de Recuperação do aluno {aluno}: ')))

    media = sum(notas) / len(notas)
    print(f'A média final de {aluno} foi {media}')
    if media >= 5:
        print(f'O aluno {aluno} foi APROVADO! Parabéns!!!')
    else:
        print(f'O aluno {aluno} foi REPROVADO!')