# Você está recebendo muitos emails de spam na sua empresa. 
# Para bloqueá-los, você deseja criar um script em Python capaz de detectar um email de spam a partir do seu domínio (o nome após o sinal de @).
# Crie uma função em Python para implementar essa funcionalidade. A função deve exibir uma mensagem de acordo com o e-mail ser spam ou não. 
# Para o exercício, considere que e-mails enviados do domínio @xyz.com são mensagens de spam.

def detectar_spam(email):
    if email.endswith('@xyz.com'):
        print(f'O e-mail é de {email} é SPAM!')
    else:
        print(f'O e-mail é de {email} não é SPAM!')

detectar_spam('usuario1@empresa.com.br')
# output:
# O email de usuario1@empresa.com não é spam.

detectar_spam('usuario1@xyz.com')
# output:
# O email de usuario2@xyz.com é spam.

# Definimos uma função chamada detectar_spam(), que recebe um endereço de e-mail como argumento. 
# Dentro da função, usamos o método de string .endswith() para verificar se o endereço de e-mail termina com o domínio "@xyz.com". 
# Em seguida, com base no resultado dessa comparação, exibimos a mensagem avisando se o e-mail é de spam ou não.