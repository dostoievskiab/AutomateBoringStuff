def vamosLa(lista):
    txtFinal = ''
    for i in range(len(lista)-2):
        txtFinal += lista[i] + ', '
    txtFinal += lista[-2] + ' e ' + lista[-1]
    return txtFinal

print(vamosLa(['macarrao', 'feijao', 'arroz', 'etudoqueadebom']))
