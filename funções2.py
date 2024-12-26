# def contar(num = 11, caractere = '+'): # Código atribuido dentro da lista de argumentos
#     for i in range(1, num):
#         print(caractere)
    
# if __name__ == '__main__':
#     contar(num = 6, caractere = '=') # Código pode ser representado pelas duas opções
#     contar(3, '¨')
#     contar('#', 7) # Para caso de inversão de parâmetro ficando fora de ordem, esse modo ocorrerá erro

x = 5
y = 6
z = 3

def soma_mult(a, b, c=0):
    if c == 0:
        return a * b
    else:
        return a + b + c

if __name__ == '__main__':
    res = soma_mult(x, y)
    print(res)
    res = soma_mult(x, y, z)
    print(res)