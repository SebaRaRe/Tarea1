from random import randrange

def sattoloCycle(items):
     i = len(items)
     while i > 1:
         i = i - 1
         j = randrange(i)
         items[j], items[i] = items[i], items[j]
     return 

cantidad = int(raw_input('Escriba un tamano para el arreglo aca: '))
A=[]
i=0
for i in range(cantidad):
    A.append(i)
sattoloCycle(A)

archivo_n = raw_input('Escriba un nombre para el archivo aca: ')
archivo = open('%s.txt'% archivo_n,'w')
for x in A:
    archivo.write('%s \n' % A[x])
archivo.close()
