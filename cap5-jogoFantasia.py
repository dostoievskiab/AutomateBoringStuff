teste = {'Espada de Aco': 1,
            'Casaco Gelido': 1,
            'Moeda de Ouro': 23,
            'Moeda de Bronze': 234,
            'Maca': 5}

loot = ['Maca','Escama de Dragao','Moeda de Ouro','Moeda de Ouro']

def displayInventory(inv):
    qtdItens = 0
    for x,y in inv.items():
        print(x, end=": ")
        print(y)
        qtdItens += 1
    print('Total de Itens: ' + str(qtdItens))

def adicionarInv(inv, itensLoot):
    for i in itensLoot:
        if i in inv:
            inv[i] += 1
        else:
            inv.setdefault(i, 1)
    return inv

seila = adicionarInv(teste, loot)
displayInventory(seila)
