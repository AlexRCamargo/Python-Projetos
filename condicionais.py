# Simples, Composto, Encadeado (Aninhado)

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

# Calcular a média aritmética das notas
media = (n1 + n2) / 2

if(media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif(media >=5):
    print("Você está de Reuperação")
else:
    print("Aluno reprovado...")

print('Sua média é {}'.format(media))   

