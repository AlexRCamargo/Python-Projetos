planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)
print(len(planeta_anao))  

# for astro in planeta_anao:
#     print(astro.upper())

# astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua']
# print(astros, end = ' ')
# astro_set = set(astros)
# print(astro_set)

astros1 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Cometa Halley'}
# print(astros1 != astros2)
# print(astros1 | astros2)
# print(astros1.union(astros2))

# print(astros1 & astros2)
# print(astros1.intersection(astros2))

# print(astros1 ^ astros2)
# print(astros1.symmetric_difference(astros2))

astros1.add('Sol')
astros1.add('Urano')
astros1.remove('Io')
astros1.discard('Lua')
astros1.pop()
astros1.clear()
print(astros1)