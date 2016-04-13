#solucion simple de k-esimo
import timeit

def mergesort(lista):
    resultado = []
    if len(lista) < 2:
        return lista
    mid = len(lista)/2
    izq = mergesort(lista[:mid])
    der = mergesort(lista[mid:])
    while (len(izq) > 0) or (len(der) > 0):
        if len(izq) > 0 and len(der) > 0:
            if izq[0] > der[0]:
                resultado.append(der[0])
                der.pop(0)
            else:
                resultado.append(izq[0])
                izq.pop(0)
        elif len(der) > 0:
            for i in der:
                resultado.append(i)
                der.pop(0)
        else:
            for i in izq:
                resultado.append(i)
                izq.pop(0)
    return resultado

def k_esimosimple(k,array):
        if k == 0:
	        print "k es invalido"
        else :
            nuevo=mergesort(array)
            return nuevo[k-1]
j=raw_input('Ingresar nombre de archivo a probar sin extension(input): ')
archivo = open('%s.txt'%j, 'r')
A = []
for linea in archivo:
	 numero = int(linea)
	 A.append(numero)
archivo.close()
print "todo va bien"

k=int(raw_input('Ingrese el valor de k: '))
print "todo va bien"
a = k_esimosimple(k,A)
print "todo va bien"
print a
times = 1   
tiempo = timeit.Timer(lambda: k_esimosimple(k,A), "")
tiempof = tiempo.repeat(times, 1)
print tiempof