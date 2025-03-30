# Seu objetivo é encontrar o segundo maior valor da lista (supondo que ela possua pelo menos dois elementos).

numeros = [90, 85, 70, 60, 45, 35, 20, 10, 5]

numeros.sort()                                             # Nessa solução, utilizamos o método .sort() para ordenar a lista numeros em ordem crescente. 
segundo_maior = numeros[-2]                                 # Uma vez feita essa ação, podemos encontrar o segundo maior elemento realizando uma indexação na lista. 
ultimo_maior = numeros[-9]

print('O segundo maior valor da Lista é:', segundo_maior)
print('O menor valor da Lista é:', ultimo_maior)

# Note que o método .sort() opera diretamente sobre a lista, portanto não é preciso guardar nenhum resultado em uma variável.
# Como os valores foram ordenados, o segundo maior valor corresponderá ao penúltimo elemento da lista, no qual acessamos pela indexação numeros[-2]. 
# Em seguida, basta exibi-lo para resolver o exercício.