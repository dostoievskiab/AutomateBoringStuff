#Search for pattern (99) 9999-9999 from clipboard then print list with all matchs
import re,pyperclip
clipboard = pyperclip.paste()
print(clipboard)
condTelefone = re.compile(r"\(\d{2}\)\s\d{4}-\d{4}")
teste = condTelefone.findall(clipboard)
print(teste)
