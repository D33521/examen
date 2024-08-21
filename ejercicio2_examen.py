#este ejercicio determina si en una cadena existen 2 o mas vocales
arreglo = ['pan', 'queso', 'chocolate',]
vocales = 'aeiou'
cadenas_con_vocales = []

for cadena in arreglo:
    conteo_vocales = 0
    cadena = cadena.lower()
    for letra in cadena:
        if letra in vocales:
            conteo_vocales += 1
    if conteo_vocales >= 2:
        cadenas_con_vocales.append(cadena)
if cadenas_con_vocales:
    print("Las cadenas que contienen 2 o más vocales son:")
    for cadena in cadenas_con_vocales:
        print(cadena)
else:
    print("Ninguna cadena contiene 2 o más vocales.")
