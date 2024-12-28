from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass # Significa estar vázio, ignorar e seguir adiante. 
             # Usado quando estiver criando uma base de código, que num determinado momento exato, 
             # não será preenchido o código do bloco, mas é necessário testar a aplicação sem erros 

if __name__ == '__main__':
    try:
        num = int(input('Digite um número positivo: '))
        if num < 0:
            raise NumeroNegativoError
    except NumeroNegativoError:
        print('Foi fornecido um número negativo.')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print(f'Fim do cálculo.')
        
