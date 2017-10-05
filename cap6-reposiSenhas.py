#!/usr/bin/python3
#Simply Password Manager (Not secure!)
import sys,pyperclip

password = { 'email' : 'huehue123',
            'blog': '123huehue',
            'website': 'vamosla123'}

if len(sys.argv) < 2:
    print('Exemplo: cap6-reposiSenhas.py [CONTA]')
    sys.exit()
conta = sys.argv[1]

if conta in password:
    pyperclip.copy(password[conta])
    print('Senha para' + conta + ' copiada para o clipboard.')
else:
    print('Nao existe a conta inserida...')
