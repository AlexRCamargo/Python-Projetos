# Tratar divisão por 0

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))

# try:        
#     r = round(n1 / n2, 2)
# except ZeroDivisionError:
#     print(f'Não é possível dividir por Zero!')
# else:
#     print(f'Resultado: {r}')

def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__': # Corpo Principal da Função
    while True: # Laço infinito
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print('Ocorreu um erro ao ler o valor. Tente novamente.')

    try:        
        r = round(n1 / n2, 2)
    except ZeroDivisionError:
        print(f'Não é possível dividir por Zero!')
    except:
        print(f'Ocorreu um erro desconhecido...')
    else:
        print(f'Resultado: {r}')
    finally:
        print('\nFim do Cálculo.')