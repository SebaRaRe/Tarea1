import heapq
import timeit
def topmMejorado(m,array):
	arrayO = array[:]
	heapq.heapify(arrayO) 
	return [heapq.heappop(arrayO) for i in range(m)]

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
#print a
times = 1   
tiempo = timeit.Timer(lambda: topmMejorado(m,A), "")
tiempof = tiempo.repeat(times, 1)
print tiempof
		

