# Manipulação de arquivos de texto

manipulador = open('arquivo.txt', 'r', encoding='utf-8') # Objeto

# print(f'\nMétodo read():\n')
# print(manipulador.read())

# print(f'\nMétodo readline():\n')
# print(manipulador.readline()) # Retorna a primeira linha do texto
# print(manipulador.readline()) # Retorna a segunda linha do texto

# print(f'\nMétodo readlines():\n')
# print(manipulador.readlines())
texto = input('Qual texto deseja procurar no arquivo? ')
try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8') # Objeto
    for linha in manipulador:
        linha = linha.rstrip() # Retira o último caractere da linha (\n)
        if texto in linha:
            print(f'A string foi encontrada!')
            print(linha)
        else:
            print(f'String não encontrada!')
except IOError:
    print(f'Não foi possivel abrir o arquivo') 
else:
    manipulador.close() # Importante sempre fechar o arquivo ao final da utilização da rotina

# Escrever em arquivos de texto

texto = '\nPython é usado em Ciência de Dados extensivamente.'
try:
    manipulador = open('arquivo.txt', 'a', encoding='utf-8')
    manipulador.write(texto)
except IOError:
    print(f'Não foi possivel abrir o arquivo') 
else:
    manipulador.close()

frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola']

# Criar e Gravar o arquivo
try:
    manipulador = open('frutas.txt', 'w', encoding='utf-8')
    manipulador.writelines(frutas)
except IOError:
    print(f'Não foi possivel abrir o arquivo') 
else:
    manipulador.close()

#Ler o arquivo criado
try:
    manipulador = open('frutas.txt', 'r', encoding='utf-8')
    print(manipulador.read())
except IOError:
    print(f'Não foi possivel abrir o arquivo') 
else:
    manipulador.close()
