#!/usr/bin/python3
#Como usar: python3 cap8-mcb.py save <palavra> - Salva clipboard na palavra-chave.
#           python3 cap8-mcb.py <palavra> - Carrega clipboard com o mesmo nome.
#           python3 cap8-mcb.py list - Lista todas as palavras salvas.
#           python3 cap8-mcb.py delete <palavra> - Deleta clipboard salvo.
#           python3 cap8-mcb.py deleteall - Deleta todos clipboard salvos.

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
print(str(sys.argv[1]))
if sys.argv[1] == 'save' and len(sys.argv) == 3:
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(str(sys.argv[2]) + ' salvo.')
elif sys.argv[1] == 'delete' and len(sys.argv) == 3:
    del mcbShelf[sys.argv[2]]
    print(str(sys.argv[2]) + ' deletado.')
elif len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        #I was using linux when coding this script... i find more convenient
        #printing the output instead of saving it in the clipboard like in the book
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1] == 'deleteall':
        mcbShelf.clear()
        print('Todos os clipboards salvos foram deletados.')

mcbShelf.close()
