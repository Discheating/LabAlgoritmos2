# 1.Ler uma lista
# de 5 números inteiros e mostre cada número juntamente com a sua posição na
integer_list = []
for i in range(5):
    integer = int(input("Insira um número inteiro: "))
    integer_list.append(integer)

print("Liste os elementos com suas posições:")
for i in range(len(integer_list)):
    print("O número {} está na posição {} da lista.".format(integer_list[i], i))







