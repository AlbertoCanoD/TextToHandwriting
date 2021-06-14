import pywhatkit as kit

print("\033[1;32;40m Bright Green  \n")

print("\033[0;31;40m Normal text\n")

texto = input('Introduzca el texto: ')

st = input('Introduzca el titulo imagen: ' ) + '.png'

print('\nA continuacion, puede elegir los colores siguiendo el formato RGB')

print('\033[0;31;40m Color rojo:\n')
colorR = input('\033[0;31;40mColor rojo: ')

colorG = input('\nColor verde: ')

colorB = input('\nColor azul: ')

#Default color is blue

def colorDefault():
    colorR = 0
    colorG = 0
    colorB = 255
    print('leche')

if(colorR.isnumeric or colorG.isnumeric or colorB.isnumeric == False): 
    colorDefault

if(0 <= (colorR or colorG or colorB) <= 255):
    colorR = 0
    colorG = 0
    colorB = 255

kit.text_to_handwriting(texto,st,[colorR, colorG, colorB,])