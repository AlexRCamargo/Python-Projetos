# Estruturas de decisões e iteração

# Implemente um programa que utilize estruturas de decisões (if, else, elif) para determinar se um número inserido pelo usuário é positivo, negativo ou zero. 
# Utilize também loops para pedir novos números até que o usuário insira X.

numero = int(input('Digite um número qualquer: '))
        
if numero <= -1:
    print(f'O número digitado {numero} é negativo!')    
elif numero >= 1:
    print(f'O número digitado {numero} é positivo!')  
else:
    print(f'O número digitado {numero} é neutro!')    
          
