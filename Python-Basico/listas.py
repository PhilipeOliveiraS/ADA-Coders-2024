# > Listas

# Antes
notas1 = 7.9
notas2 = 9.7
notas3 = 8.5

# Depois com listas
notas = [7.9, 9.7, 8.5]


# Criando listas
lista = []
lista = list()
lista = [26, 'Philipe', 3.23546, False]
lista_de_listas = [10, [1, 2, 3]]


# Indexação e Slice(fatiamento)

lista = [10, 'Philipe', 3.235546, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])
print(lista[3: ])
print(lista[2:6:2])

# > Iterações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os indices

print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])


# > MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

# Append

print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)

# insert

lista.insert(2, 10)

print('Depois do insert: ', lista)


# extend

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend: ', lista)

# pop

lista.pop()
print('Depois do pop: ', lista)

lista.pop(0)
print('Depois do pop: ', lista)

# remove

lista.remove(3)

print('Depois do remove: ', lista)

# count

print('Quantidade de 2 na lista: ', lista.count(2))

# index

print('O índice do elemento 12 é: ', lista.index(12))

# sort

lista.sort()
print(lista)

# reverse

lista.sort(reverse=True)
print(lista)

# FUNÇÕES PARA LISTAS

# LEN

print('Comprimento da lista: ', len(lista))

# sum

print('Soma dos elementos da lista: ', sum(lista))

# max

print('Maior elemento da lista: ', max(lista))

# min

print('Menor elemento da lista: ', min(lista))