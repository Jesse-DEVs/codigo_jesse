import string 
import random 


def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = []
    for i in range(comprimento):
        caractere = random.choice(caracteres) 
        senha.append(caractere)

    return ''.join(senha)
Tamanha_da_senha = int(input('Digite o tamanho da senha: ')
senha = gerar_senha(Tamanho_da_senha)
print(senha)
