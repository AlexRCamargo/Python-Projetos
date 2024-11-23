# Digitação das notas, divulgação das variaveis
nota1 = float(input('Digite a nota do 1º Bimestre: '))
nota2 = float(input('Digite a nota do 2º Bimestre: '))
nota3 = float(input('Digite a nota do 3º Bimestre: '))
nota4 = float(input('Digite a nota do 4º Bimestre: '))

# Calculo da média final
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibição da média
print('A média final é: ',media)

# verificação se o aluno está aprovado, reprovado ou de exame
if(media>=6):
    print('Você está Aprovado!!!')
    print('Parabéns!!!')
elif(media<5):
    print('Você está Reprovado!')
else:
    print('Você está de Exame.')
    print('Comece a estudar já! Boa sorte!!!')

print('A sua média é {}'.format(media))  
