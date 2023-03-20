# Exercícios Listas
# A partir da seguinte lista:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Intervalo de 1 a 9
# Intervalo de 8 a 13
# Números pares
# Números ímpares
# Todos múltiplos de 2, 3 e 4
# Lista reversa
# Razão entre a soma do interval de 10 a 15 pelo intervalo de 3 a 9 em float

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def menu():
    print("# Exercícios Listas #")
    print("1 - Intervalo de 1 a 9\n2 - Intervalo de 8 a 13\n3 - Números pares\n4 - Números ímpares\n5 - Todos múltiplos de 2, 3 e 4\n6 - Lista reversa"
          "\n7 - Razão entre a soma do interval de 10 a 15 pelo intervalo de 3 a 9 em float\n8 - Sair")
    opc = int(input("Qual opção deseja usar: "))
    return opc


def rangeOptionOne(list):
    resultList = list[1:10]
    print(resultList)
    return resultList, list

def rangeOptionTwo(list):
    resultListTwo = list[9:14]
    print(resultListTwo)
    return resultListTwo, list

def pairNumbers(list):
    for num in list:
        if num % 2 == 0:
            print("Números pares: {}".format(num))
    return num, list

def oddNumbers(list):
    for num in list:
        if num % 2 == 1:
            print("Números impares: {}".format(num))
    return list, num

def allMultiples(list):
    for num in list:
        if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
            print("Todos múltiplos de 2, 3 e 4: {}".format(num))
    return list

def reverseList(list):
    reversedList = list[::-1]
    print(reversedList)
    return list


opc2 = 0
while opc2 != 10:
    opc = menu()
    if opc == 1:
        rangeOptionOne(list)
    elif opc == 2:
        rangeOptionTwo(list)
    elif opc == 3:
        pairNumbers(list)
    elif opc == 4:
        oddNumbers(list)
    elif opc == 5:
        allMultiples(list)
    elif opc == 6:
        reverseList(list)
    elif opc == 7:
        print("Em construção!")
    elif opc == 8:
        exit("Obrigado por usar nosso Software!")
    else:
        print("Opção escolhida invalida!")















