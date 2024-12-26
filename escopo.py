# Escopo Global e Local

var_global = 'Curso Completo de Python'

def escreve_texto():
    global var_global # Atribuir valor somente após inserir a atribuição de valor
    var_global = 'Banco de dados com SQL' # Foi criada uma nova variável de escopo local com o nome da variável externa global
    var_local = 'Alexsander Camargo'
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')
    # print(f'Variável Local: {var_local}') - Variável inacessivel fora da função


