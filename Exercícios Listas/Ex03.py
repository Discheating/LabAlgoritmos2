# 3.Ler uma lista
# de 4 números e mostre o menor e maior número da lista;
list = []
for i in range(4):
    num = float(input("Digite um número: "))
    list.append(num)

bigger = list[0]
smaller = list[0]

for num in list:
    if num > bigger:
        bigger = num
    if num < smaller:
        smaller = num

print("O maior número da lista é:", bigger)
print("O menor número da lista é:", smaller)