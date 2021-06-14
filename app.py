import pywhatkit as kit

texto = input('Introduzca el texto: ')

color = input('Introduzca los colores en formato R,G,B: ')

st = input('Introduzca el titulo imagen: ')

titulo = st + '.png'

#kit.text_to_handwriting(texto,titulo + formato,list = (255,0,0))


kit.text_to_handwriting(texto,titulo)