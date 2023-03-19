#2.Ler uma lista#
#de 10 números reais e mostre-os na ordem inversa;#
integer_list = []
for i in range(10):
    integer = int(input("Insira um número inteiro: "))
    integer_list.append(integer)

print("Liste os elementos com suas posições na ordem inversa:")
for i in range(len(integer_list)-1, -1, -1):
    print("O número {} está na posição {} da lista.".format(integer_list[i], i))