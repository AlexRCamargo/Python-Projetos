def fatorial(numero):
    if numero < 0:
        return 'Digite um valor maior ou igual a zero'
    else:
        if numero==0 or numero==1:
            return 1
        else:
            return numero * fatorial(numero - 1)