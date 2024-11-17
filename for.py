# lista = [0, 2, 5, 8, 9, 4, 3, 1, 7,6]
# palavra = 'Corinthians'
# for item in lista:
#     print(item)
# for letra in palavra:
#     print(letra)

# for numero in range(1,11):
#     print(numero)

# nome = input('Digite o seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}')

# range(valor_inicial, valor_final, incremento)
# for x in range(2,20,3):
#     print(x)
# for x in range(20,2,-3):
#     print(x)

pedras = ('Rubi','Esmeralda','Quartzo','Safira','Diamante','Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)