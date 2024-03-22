lista=[12,22,33,44,55,66,77,88,98]

for i in range(0, len(lista)):
    if (lista[i] % 2)== 0:
        print(lista[i])
    #tambien anda sin esto:
    else:
        continue