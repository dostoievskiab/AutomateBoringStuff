#Function for Collatz Conjecture
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Escreva o numero: ')
try:
    numeroDig = int(input())
    #Calling function until 1
    while numeroDig != 1:
        numeroDig = collatz(numeroDig)
        print(str(numeroDig))
except ValueError:
    print('ERRO!!!! Voce escreveu uma string, escreva apenas integer')
