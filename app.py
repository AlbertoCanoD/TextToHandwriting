import pywhatkit as kit

texto = input('Introduzca el texto: ')

st = input('Introduzca el titulo imagen: ' ) + '.png'

color = input('Introduzca los colores en formato R,G,B: ')

kit.text_to_handwriting(texto,st)