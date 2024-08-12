# este programa calcula si en una lista no existen elementos repetidos 
lista = (1,2,3,4,5,6,7,8,9,1,4,5)
a=0
i=0
while i<len(lista):
    b=lista[i]
    if lista.count(b) > 1:
        a=a+1
    i=i+1
print("el numero de elementos repetidos es: ")
print (a/2)







