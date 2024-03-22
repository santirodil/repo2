cant = int(input('Cuantos numeros va a ingresar? '))

# incicializa la lista con valores en 0 y con cantidad de posiciones segun cant
lista = [0] * cant 

for i in range(0,cant):
    lista[i] = int(input('Ingrese un numero '))

for i in range(0,cant):
    if(lista[i] < 0):
        break
    print(str(lista[i]))
    
