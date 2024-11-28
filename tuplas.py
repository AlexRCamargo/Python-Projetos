# São imutáveis

tupla = (2,4,6,8,3,5,7,9)
print(tupla)
halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres # Contatenação
print(halogenios)
print(elementos)
print(len(tupla))
print(len(halogenios))

# t1 = (5, 6, 4, 8, 22, 56, 5, 6, 3, 2, 4, 5, 7)
# print(t1.count(5))

print(halogenios[0:2])
print('Cl' in halogenios)

# Operações não disponiveis em tuplas .sort(), .append(), .reverse(), .pop(), ...

# for elemento in elementos:
#     print(f'Elemento quimico: {elemento}')

# grupo17 = list(halogenios)
# grupo17[0] = 'H'
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'] # Lista
alcalinos = tuple(grupo1)
print(type(alcalinos))
print(sorted(alcalinos))