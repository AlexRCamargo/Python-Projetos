n1 = float(input('Digite a nota do 1º Bimestre: '))
n2 = float(input('Digite a nota do 2º Bimestre: '))
n3 = float(input('Digite a nota do 3º Bimestre: '))
n4 = float(input('Digite a nota do 4º Bimestre: '))

# Calculo da média final
media = (n1 + n2 + n3 + n4) / 4

# Exibição da média
print('A média final é: ',media)

# verificação se o aluno está aprovado, reprovado ou de exame
if(media>=7):
    print('Resultado: Aprovado.')
    print('Parabéns!!!')
elif(media<5):
    print('Você está Reprovado!')
else:
    print('Você está de Recuperação.')
    print('Comece a estudar já! Boa sorte!!!')

print('A sua média é {}'.format(media)) 
