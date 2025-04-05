
temperaturas = []
total = 0

for i, t in enumerate(temperaturas):
    if t < 0:
        total += 1
print(f'Há {total} temperaturas negativas na amostra.')

temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
total = 0

for i, t in enumerate(temperaturas):
    if t < 0:
        print(f'A temperatura em {i} é negativa, com {t}°C.')