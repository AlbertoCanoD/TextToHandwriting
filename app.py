import pywhatkit as kit

texto = input('Introduzca el texto: ')

st = input('Introduzca el titulo imagen: ' ) + '.png'

print('\nA continuacion, puede elegir los colores siguiendo el formato RGB')

colorR = input('\033[0;31;40mColor rojo: ')

colorG = input('\nColor verde: ')

colorB = input('\nColor azul: ')

#Default color is blue
if(colorR or colorG or colorB == ''):
    colorR = 0
    colorG = 0
    colorB = 255

kit.text_to_handwriting(texto,st,[colorR, colorG, colorB,])