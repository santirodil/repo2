cant = int(input('Cuantos numeros va a ingresar? '))

# incicializa la lista con valores en 0 y con cantidad de posiciones segun cant
lista = [0] * cant 

for i in range(0,cant):
    lista[i] = int(input('Ingrese un numero '))

cadena = ''
cadena2 = ''

for i in range(0,cant):
    if not(int(lista[i]) % 3 == 0):
        cadena2=str(cadena) + str(lista[i])#esta cadena2 es para que no ponga un guion de mas al final
        cadena=str(cadena) + str(lista[i]) + str('-')

print(cadena2)