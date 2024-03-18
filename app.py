numero_valido='False'

while numero_valido=='False':

    menu= """ Menú de opciones
                1) Saber si un numero es par
                2) Dividir un numero por otro
            """
    print (menu)

    numero_menu = input('ingrese un numero para seleccionar la opcion ')
    print(numero_menu)

    if  int(numero_menu)==1:
        numero_valido='True'
        ingresado = input('ingrese un numero para saber si es par o impar ')
        print(ingresado)
        if(int((ingresado)) % 2 == 0):
            print('Es Par ')
        else:
            print('Es Impar')
    elif int(numero_menu)==2:
        numero_valido='True'
        dividendo= float(input('Ingrese el numero del dividendo '))
        print(dividendo)
        divisor= float(input('Ingrese el numero del divisor '))
        print(divisor)
        resultado= dividendo/divisor
        print('Resultado de la division: '+ str(resultado))
    #else: print('No se ingreso un numero valido. intente otra vez. ')




#a=9.99999
#b=2
##print(type(a))
#print(type(b))
#print(a / b)    #division SIEMPRE DECIMAL
#print(a // b)   #division SIEMPRE ENTERA
#c= a/b
#print (round(c))
#while i<111:
#    print('iteracion numero ' + i)
#    i+=i+1
    