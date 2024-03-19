cant = int(input('Cuantos numeros va a ingresar? '))

# incicializa la lista con valores en 0 y con cantidad de posiciones segun cant
lista = [0] * cant 

for i in range(0,cant):
    lista[i] = int(input('Ingrese un numero '))

cantpares=0
cantimpares=0
for i in range(0,cant):
    if lista[i] % 2 ==0:
        cantpares =cantpares+1
    else:
        cantimpares=cantimpares+1
#inicializo la lista de pares y la de impares
listaPares= [0]*cantpares
listaImpares= [0]*cantimpares

iPares= 0
iImpares= 0

for i in range(0,cant):
    if lista[i] % 2 ==0:
        listaPares[iPares]=lista[i]
        iPares= iPares+1
    else:
        listaImpares[iImpares]=lista[i]
        iImpares= iImpares+1
print('Numeros pares: ')
for i in range (0,cantpares):
    print(listaPares[i])
print('Numeros impares: ')
for i in range (0,cantimpares):
    print(listaImpares[i])