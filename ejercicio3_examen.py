#este programa determina que elementos tiene la primera lista que no esten en la segunda lista
lista1 = (1, 2, 3, 4, 5, 6, 7, 8)
lista2 = (3, 4, 5, 6, 7, 8, 9, 10)
set_lista2 = set(lista2)

for item in lista1:
    if item not in set_lista2:
        print(item)