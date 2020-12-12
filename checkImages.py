import os
import sys
def getListFiles(filename):
	return sorted(os.listdir(filename))

def corregirFile():
	fileClases = 'classes.names'
	with open("./custom/"+fileClases, "a") as f:
		    f.write('\n')
		    f.close()
	print('Corrigiendo el Archivo ')

def checkClass():
	fileClases = 'classes.names'
	arr = getListFiles('./custom')	
	if fileClases in arr:
		with open("./custom/"+fileClases, "r") as f:
		    file_str = str(f.read())
		    f.close()
		last_chr = file_str[-1]
		if last_chr=='\n' :
			print('Esta correcto el formato: '+ fileClases)
		else:
			print('Falta un "\\n" al final del archivo'+ fileClases)
			corregirFile()

	else:
		print('Falta el Archivo '+fileClases)




def checkImages():
	listImages = getListFiles('./custom/images/')	
	listLabels = getListFiles('./custom/labels/')
	flag = False
	for img in listImages:
			if not(img.replace('.jpg','.txt') in listLabels):
				print('La imagen:',img, 'no tiene label')
				flag = True
	if flag:
		sys.exit(1)
	if len(listImages) == len(listLabels):
		print('Tienes el  mismo numero de Imagenes y Labels :)')	
	else:
		print('Debes tener el mismo numero de Imagenes y Labels')
		sys.exit(1)
	print('Cantidad de Imagenes:',len(listImages) )
	print('Cantidad de Labels:',len(listLabels) )

checkClass()
checkImages()
sys.exit(0)


