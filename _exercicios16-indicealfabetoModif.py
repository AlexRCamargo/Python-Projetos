# Crie uma função que retorna uma letra do alfabeto, dado o seu índice. 
# Por exemplo, o índice 1 deve retornar a letra "A", o índice 2 deve retornar a letra "B" e assim por diante. 
# Caso o índice esteja acima ou abaixo dos limites do alfabeto, a função deve retornar um string vazio.

indice = int(input('Digite um número para encontrar sua letra correspondente: '))

def indice_do_alfabeto(indice):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if 1 <= indice <= 26:
        return alfabeto[indice - 1]
    else:
        return ''

print(f'A letra digitada pelo usuário foi a letra {indice_do_alfabeto(indice)}.')
# output: "A"

# print(indice_do_alfabeto(15))
# output: "C"

# print(indice_do_alfabeto(30))
# output: ""

# Na função indice_do_alfabeto(), criamos uma string chamada alfabeto, que contém todas as letras maiúsculas do alfabeto. 
# Dentro da função, verificamos se o índice está dentro do intervalo válido de 1 a 26. Se estiver, retornamos a letra 
# correspondente ao índice fornecido usando indexação de strings (note que usamos indice - 1 nesta etapa porque a 
# indexação em Python parte de zero). 
# Por outro lado, se o índice estiver fora do intervalo válido, a função retorna uma string vazia.