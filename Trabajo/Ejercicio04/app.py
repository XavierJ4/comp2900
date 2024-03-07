def promedio(lista_numeros):
    suma = 0
    for valor in lista_numeros:
        suma = suma + valor
    
    return (suma / len(lista_numeros))

lista = [90, 50, 40, 39]

print(lista)
print (f'El valor del promedio de la lista es: {promedio(lista)}')