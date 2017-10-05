import re

def passTest(password):
    if len(password) < 8:
        print('Senha possui menos que 8 caract.')
        return
    testePass = re.compile(r'[A-Z]').search(password)
    if testePass == None:
        print('Senha precisa ter ao menos 1 caracter maiusculo.')
        return
    testePass = re.compile(r'[a-z]').search(password)
    if testePass == None:
        print('Senha precisa ter ao menos 1 caracter minusculo.')
        return
    testePass = re.compile(r'\d').search(password)
    if testePass == None:
        print('Senha precisa ter ao menos 1 caracter numerico.')
        return
    print('Senha aprovada!')
    return

print('Digte sua senha: ')
senha = input()
passTest(str(senha))
