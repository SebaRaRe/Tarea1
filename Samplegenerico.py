from random import randrange 

def sattoloCycle(items):            #sattoloCycle(arreglo) recibe un arreglo y lo desordena
     i = len(items)
     while i > 1:
         i = i - 1
         j = randrange(i)
         items[j], items[i] = items[i], items[j]
     return 

cantidad = int(raw_input('Escriba un tamano para el arreglo aca: '))  #recibimos la cantidad de elementos que queremos generar
A=[]
i=0
for i in range(cantidad):    #rellenamos el arreglo 
    A.append(i)
sattoloCycle(A)              #desordenamos el arreglo

archivo_n = raw_input('Escriba un nombre para el archivo aca: ')  #asignamos el nombre que le daremos a nuestro archivo
archivo = open('%s.txt'% archivo_n,'w')                           #abre un archivo
for x in A:                                                       #rellenamos el archivo con los datos del arreglo para luego cerrar
    archivo.write('%s \n' % A[x])                                 #el archivo 
archivo.close()
