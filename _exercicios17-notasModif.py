notas = []
contador = 1

aluno = input('Digite o nome do Aluno: ')
disciplina = input('Digite o nome da matéria: ')

# Coleta das 4 notas com validação
while contador < 5:
    try:
        nota = float(input(f'Informe a nota do {contador}º bimestre do aluno {aluno}: '))
        if 0 <= nota <= 10:
            notas.append(nota)
            contador += 1
        else:
            print('A nota deve estar entre 0 e 10.')
    except ValueError:
        print('Entrada inválida. Digite um número válido.')

# Cálculo da média
media = sum(notas) / len(notas)
print(f'\nA média final de {aluno} na disciplina {disciplina} foi {media:.2f}')

# Verificação da situação do aluno
if media >= 7:
    print(f'O aluno {aluno} foi APROVADO! Parabéns!!!')
else:
    print(f'O aluno {aluno} ficou de RECUPERAÇÃO! Estude um pouco mais. Boa sorte!!!')

    # Entrada da nota de recuperação com validação
    while True:
        try:
            recuperacao = float(input(f'Informe a nota da prova de Recuperação do aluno {aluno}: '))
            if 0 <= recuperacao <= 10:
                notas.append(recuperacao)
                break
            else:
                print('A nota deve estar entre 0 e 10.')
        except ValueError:
            print('Entrada inválida. Digite um número válido.')

    # Recalcula a média com a nota da recuperação
    media = sum(notas) / len(notas)
    print(f'\nA nova média final de {aluno} foi {media:.2f}')

    if media >= 5:
        print(f'O aluno {aluno} foi APROVADO! Parabéns!!!')
    else:
        print(f'O aluno {aluno} foi REPROVADO.')