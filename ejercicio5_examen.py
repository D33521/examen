
# este programa desarrolla un algoritmo para determinar la mediana de un arreglo ordenado 
arreglo = [5,10,15,4,3,8,9,7,6]
arreglo.sort()
a=len(arreglo)
if a % 2 == 0:
    b= a//2
    print (f"la mediana del arreglo de numeros enteros es: {arreglo[b]} ")
else:
    b= (a//2) +1
    print (f"la mediana del arreglo de numeros enteros es: {arreglo[b]} ")
