for cont_ex in range(1,6):
    print(f'\nRodada: {cont_ex}')
    for cont_in in range(5, 0, -1):
        print(f'Valor: {cont_in}')
    
print('Fim dos Laços.')

import random

for A in range(1,6):
    print(f'\nConjuto {A}')
    for B in range(6):
        num = random.randint(1,60)
        print(f'Valor: {num}')