#VARIAVEIS#
def cripto(palavra):
  encripto = ""
  for letra in palavra:
    if 'a' <= letra <= 'e':
      encripto += '1'
    elif letra >= 'f' and letra <= "j":
      encripto += '2'
    elif letra >= "k" and letra <= 'o':
      encripto += '3'
    elif letra >= 'p' and letra <= 'z':
      encripto += '4'
    else:
      encripto += '5'
  return encripto
 
texto = input('Digite o texto:')
resultado =  cripto(texto.lower())
print ('Encriptado: ' + resultado)