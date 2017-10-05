table = [['apples','oranges','cherries','banana'],
          ['Alice','Bob','Carol','David'],
          ['dogs','cats','moose','goose']]
def printTable(tab):
    #First step - Length of each column
    colTam = [0] * len(tab)
    for x in range(len(tab)):
        biggest = 0
        for y in tab[x]:
            if len(y) > biggest:
                colTam[x] = len(y)

    print(colTam)

    for n in range(len(tab[0])):
        for o in range(len(tab)):
            print(tab[o][n].rjust(colTam[o]+5), end=' ')
        print()

printTable(table)
