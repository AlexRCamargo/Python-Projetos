import os

os.chdir('C:\\Teste')
print(f'Diretório Atual: {os.getcwd()}')

padrao_nome = input('Qual o padrão de nome de arquivos a usar (sem extensão)? ')

for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome + ' ' + str(contador)

        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print(f'\nArquivos Renomeados.')