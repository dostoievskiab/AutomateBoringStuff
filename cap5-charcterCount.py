import pprint

message = 'Vamos la vamos ver no que vai dar'
contador = {}

for character in message:
    contador.setdefault(character, 0)
    contador[character] += 1

pprint.pprint(contador)
