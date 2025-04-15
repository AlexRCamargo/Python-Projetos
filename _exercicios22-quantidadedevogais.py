frase = input('Digite uma frase: ''\n')
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â', 'ê', 'î', 'ô', 'û']

listas_vogais = [vog for vog in frase if vog in vogais]
print(f'A frase possui {len(listas_vogais)} vogais:')
print(listas_vogais)