import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de fallos permitidos
max_fails = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []





print("¡Bienvenido al juego de adivinanzas!")


#Dificultades
print('''Ingresa la dificultad a la que quieres jugar.
                    F : Fácil.  En la palabra a adivinar se muestran todas las vocales por defecto.
                    M : Medio.   Se muestra la primer y la última letra de la palabra.
                    D : Dificil. No se muestra ninguna letra de la palabra''')
difficulty= input().lower()
while difficulty != 'f' and difficulty != 'm' and difficulty != 'd':
    print('El caracter "'+difficulty+'" no es valido. Intente de nuevo.')
    print('''Ingresa la dificultad a la que quieres jugar.
                    F : Fácil.  En la palabra a adivinar se muestran todas las vocales por defecto.
                    M : Medio.   Se muestra la primer y la última letra de la palabra.
                    D : Dificil. No se muestra ninguna letra de la palabra''')
    difficulty= input().lower()

if difficulty=='f':
    guessed_letters.append('a')
    guessed_letters.append('e')
    guessed_letters.append('i')
    guessed_letters.append('o')
    guessed_letters.append('u')
elif difficulty=='m':
    guessed_letters.append(secret_word[0])
    guessed_letters.append(secret_word[len(secret_word)-1])
    

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

word_displayed = "_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
####print(f"Palabra: {word_displayed}")

# Mostrar la palabra parcialmente adivinada
letters = []
for letter in secret_word:
    if letter in guessed_letters:
        letters.append(letter)
    else:
        letters.append("_")

word_displayed = "".join(letters)
print(f"Palabra: {word_displayed}")

fails=0
while fails < max_fails:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    #verificar si no se ingreso un vacio
    if letter=='':
        print("No se puede ingresar vacio. Intenta de nuevo.")
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word and letter != '':
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        fails=fails+1

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_fails} intentos.")
    print(f"La palabra secreta era: {secret_word}")