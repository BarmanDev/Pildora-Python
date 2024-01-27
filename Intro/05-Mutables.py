# Las Listas, diccionarios y conjuntos son mutables

listaCervezas = ['Paulnaer','Hogarden']
print(listaCervezas)
print(id(listaCervezas))

listaCervezas.append('Cruzcampo no es cerveza')
print(listaCervezas)
print(id(listaCervezas))