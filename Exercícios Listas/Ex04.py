# 4.Crie uma
# programa que crie uma lista de números aleatórios e exiba. O tamanho da lista
# deve ser informado pelo usuário;
import random

size = int(input("Digite o tamanho da lista: "))

list = []
for i in range(size):
    list.append(random.randint(1, 100))

print("Lista de números aleatórios:")
print(list)