#solucion simple de k-esimo
import timeit   #para medir tiempo
def mergesort(lista):     #implementacion merge
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
        if k == 0:           #aca se verifica si k es cero y se imprime k es invalido
	        print "k es invalido"
        else :
            nuevo=mergesort(array)   #si k no es cero, nuevo es = a la funcion merge con el arreglo y lo devuelve ordenado
            return nuevo[k-1]        #devuelve el k menos uno porque e los arreglo tenemos la posicion 0
j=raw_input('Ingresar nombre de archivo a probar sin extension(input): ') #con esta funcion igualamos a j una entrada de teclado
archivo = open('%s.txt'%j, 'r')   #abre y lee el archivo ya creado        #usaremos por ejemplo "cienmil" "doscientosmil"
A = []                            #lista vacia
for linea in archivo:             #pasa los elemntos del archivo al arreglo vacio
	 numero = int(linea)
	 A.append(numero)
archivo.close()                   #cerramos el archivo
print "todo va bien"              #verificador

k=int(raw_input('Ingrese el valor de k: '))    #recibimos el k por teclado y queda casteado a int
print "todo va bien"
a = k_esimosimple(k,A)                         # instanciamos la funcion k_esimosimple
print "todo va bien"
print a
times = 1                                              #estas ultimas 4 lineas deen ir para contabilizar el tiempo que tarda la funcion
tiempo = timeit.Timer(lambda: k_esimosimple(k,A), "")
tiempof = tiempo.repeat(times, 1)
print tiempof
