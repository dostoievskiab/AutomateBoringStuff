#Search for pattern (99) 9999-9999 from clipboard then print list with all matchs
import re,pyperclip
clipboard = pyperclip.paste()
Telefones = re.compile(r"\(\d{2}\)\s\d{4}-\d{4}").findall(clipboard)

for n in range(len(Telefones)):
    print(Telefones[n])

if len(Telefones) > 0:
    print('Encontrado ' + str(len(Telefones)) + ' numeros telefonicos.')
else:
    print('Verifique se voce copiou (Ctrl+C) algo antes de rodar o programa.')
