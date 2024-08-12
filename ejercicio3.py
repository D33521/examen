
# desarrollar un programa que dadas 2 listas determine que elementos tiene la primera lista que no tenga la senguda lista
lista1 = (1,2,3,4,5,6,7,8)
lista2 = (3,4,5,6,7,8,9,10)
i=0
j=0
a=0
while i<len(lista1):
    while j<len(lista2):
        if lista1[i] == lista2[j]: 
            a=a+1
        j=j+1
    if a==0:
        print (lista1(i))
    i=i+1
    j=0

    
        
           
            