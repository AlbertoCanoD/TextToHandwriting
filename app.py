import pywhatkit as kit

texto = input('Introduzca el texto: ')

st = input('\nIntroduzca el titulo imagen: ' ) + '.png'

def colores():
    numero = -1
    while numero < 0:
        try:
            numero = int(input())
        except:
            print('El rango es 0-255')
            pass
    return numero

print('\nA continuacion, puede elegir los colores siguiendo el formato RGB')

print('\nColor rojo(0-255): ', end="")

colorR = colores()

print('Color verde(0-255): ', end="")

colorG = colores()

print('\nColor azul(0-255): ', end="")

colorB = colores()

try:
    kit.text_to_handwriting(texto,st,[colorR, colorG, colorB,])
except:
    print('Error al crear la imagen')