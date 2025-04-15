# Manipulação de strings

# Escreva um programa que receba uma frase do usuário e conte quantas palavras ela possui. Em seguida, inverta a ordem das palavras na frase.

frase = input('Digite uma frase qualquer: ')                        # Solicita ao usuário que digite uma frase

palavras = frase.split()                                            # Divide a frase em palavras utilizando espaço como separador

total_palavras = len(palavras)                                      # Conta o número de palavras

print(f'O texto digitado possui {total_palavras} palavras.')        # Exibe o número de palavras

palavras_invertidas = palavras[::-1]                                # Inverte a ordem das palavras

frase_invertida = ' '.join(palavras_invertidas)                     # Junta novamente as palavras invertidas em uma string

print(f'A frase com as palavras invertidas é: {frase_invertida}')   # Exibe a frase com a ordem das palavras invertida

# Passo 1: Preparar o Texto de Exemplo
# Primeiro, precisamos de uma frase ou um texto para trabalhar. Você pode usar qualquer texto, mas para este exemplo, vamos usar uma frase simples:
# texto_exemplo = "Olá, como vai você? Como você está hoje? Hoje está um lindo dia!"
# Passo 2: Dividir o Texto em Palavras
# Python torna incrivelmente fácil dividir um texto em suas palavras constituintes. Usamos o método .split(), que separa uma string em uma lista de palavras, 
# usando espaços como delimitadores padrão.
# palavras = frase.split()
# Após essa operação, palavras é uma lista onde cada elemento é uma palavra do texto_palavras.
# Passo 3: Contar as Palavras
# Agora que temos nossa lista de palavras, podemos contar quantas palavras existem simplesmente usando a função len(), que retorna o tamanho de uma lista.
# total_palavras = len(palavras)
# Passo 4: Exibir o Resultado
# Finalmente, vamos imprimir o total de palavras encontradas na frase.
# print('O texto digitado possui {total_palavras} palavras.')
# Conclusão
# Contar palavras em Python é uma tarefa simples, mas fundamental, que pode servir como base para operações mais complexas de processamento de texto. 
# Seja você um escritor procurando uma maneira rápida de contar palavras em seus artigos ou um desenvolvedor explorando a análise de texto, 
# Python oferece as ferramentas necessárias para realizar essa tarefa de maneira eficiente.