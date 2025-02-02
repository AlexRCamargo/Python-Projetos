nome = string()

while True:
    print('Digite o nome do aluno ou X para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break

n1 = float(input('Digite a nota do aluno no 1º Bimestre: '))
n2 = float(input('Digite a nota do aluno no 2º Bimestre: '))
n3 = float(input('Digite a nota do aluno no 3º Bimestre: '))
n4 = float(input('Digite a nota do aluno no 4º Bimestre: '))
f1 = float(input('Digite a quantidade de faltas do aluno: '))

# Calculo da média final
media = (n1 + n2 + n3 + n4) / 4

# Exibição da média
print('A média final é: ',media)

# verificação se o aluno está aprovado, reprovado ou de exame
if(media>=7):

    print('Resultado: Aprovado. Parabéns!!!')
elif(media<5):
    print('Você está Reprovado!')
else:
    print('Você está de Recuperação. Comece a estudar já! Boa sorte!!!')
    
print('A sua média é {}'.format(media)) 
