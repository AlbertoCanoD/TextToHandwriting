# Para retardar el cierre de la consola
import time

import pywhatkit as kit

# Texto a transcribir
texto = input('Introduzca el texto: ')

# Titulo de la imagen en formato png
st = input('\nIntroduzca el titulo imagen: ') + '.png'

# Para asegurarnos que introducimos un entero para el rango de colores
def colores():
    numero = -1
    while numero < 0:
        try:
            numero = int(input())
        except:
            pass
    return numero

# Aplicacion principal
def main():

    print('\nA continuacion, puede elegir los colores siguiendo el formato RGB')

    # Color red method
    def rojo():

        print('\nColor rojo(0-255): ', end="")

        colorR = colores()

        if(colorR > 255):
            print('\nEl rango de valores es 0-255')
            rojo()
        return colorR

    # Color green method
    def verde():

        print('\nColor verde(0-255): ', end="")

        colorG = colores()

        if(colorG > 255):
            print('\nEl rango de valores es 0-255')
            verde()
        return colorG

    # Color blue method
    def azul():

        print('\nColor azul(0-255): ', end="")

        colorB = colores()

        if(colorB > 255):
            print('\nEl rango de valores es 0-255')
            azul()
        return colorB

    try:
        kit.text_to_handwriting(texto, st, [rojo(), verde(), azul(), ])
    except:
        print('\nError al crear la imagen')
        #Recursive call
        main()
    else:
        print('\nImagen creada con exito!!!')
        time.sleep(3)

main()
