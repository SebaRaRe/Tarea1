
import timeit

import heapq 

#siguiente funcion del codigo documentado en bibliografia

def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(heapq.merge(left, right))
	
def topmMejorado(m,array):  
        if m == 0:           #aca se verifica si k es cero y se imprime k es invalido
	        print "m es invalido"
        else :
            nuevo=merge_sort(array)   #si k no es cero, nuevo es = a la funcion merge con el arreglo y lo devuelve ordenado
            return nuevo[:m] 

j=raw_input('Ingresar nombre de archivo a probar sin extension(input): ')
archivo = open('%s.txt'%j, 'r')
A = []
for linea in archivo:
	 numero = int(linea)
	 A.append(numero)
archivo.close()
print "todo va bien"

m=int(raw_input('Ingrese el valor de m: '))
print "todo va bien"
a = topmMejorado(m,A)
print "todo va bien"
print a
times = 1   
tiempo = timeit.Timer(lambda: topmMejorado(m,A), "")
tiempof = tiempo.repeat(times, 1)
print tiempof
		

