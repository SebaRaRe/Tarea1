import timeit

def partition2(arr, left, right, pivot): 
	swapIndex=left 
	for i in range(left, right+1): 
		if arr[i]<pivot: 
			arr[i], arr[swapIndex] = arr[swapIndex], arr[i] 
			swapIndex+=1 
	return swapIndex-1   

def mediana(arr, left, right, k): 
	length=right-left+1 
	if not 1<=k<=length: 
		return 
	if length<=5: 
		return sorted(arr[left:right+1])[k-1]   
				
	numMedians=length/5 
	medians=[mediana(arr, left+5*i, left+5*(i+1)-1, 3) for i in range(numMedians)] 
	pivot=mediana(medians, 0, len(medians)-1, len(medians)/2+1) 
	pivotIndex=partition2(arr, left, right, pivot) 
	rank=pivotIndex-left+1 
	if k<=rank: 
		return mediana(arr, left, pivotIndex, k) 
	else: 
		return mediana(arr, pivotIndex+1, right, k-rank) 


def k_esimoMejorado(k,array):
        if k == 0:
	        print "k es invalido"
        else:
            valor=mediana(array,0,len(array)-1,k)
            return valor
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
a = k_esimoMejorado(k,A)
print "todo va bien"
print a
times = 1   
tiempo = timeit.Timer(lambda: k_esimoMejorado(k,A), "")
tiempof = tiempo.repeat(times, 1)
print tiempof