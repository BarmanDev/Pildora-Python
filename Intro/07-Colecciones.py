#Tuplas no pueden ser modificados despues de su creación (inmutables)
tupla = (1,'dos', 3.0)
print(tupla)
print(tupla[2])

#Listas: pueden ser modificados agregados o eliminados despues de su creación (mutables)
lista = [1, 'dos', 3.0]
print(lista)
lista.append('Python mola mazo')
print(lista[3])

#Conjuntos(set): coleciones no ordenadas de elementos únicos pueden ser añadidos o eliminados despues (mutables)
conjunto = {1,2,3,1,2,3}
print(conjunto)

#Frozenset: Similar al ser pero no se puede agregar ni eliminar elementos
conjunto_frozenset = frozenset({"Let it go", "Let it go", "Can't hold it back anymore"})
print(conjunto_frozenset)

#Diccionarios dict: Son colecciones con clave valor que pueden ser añadidos, modificados o eliminados después
diccionario = {'dia-1': 'Sonrie 14 minutos', 'dia-2': 'optimismo inteligente'}
print(diccionario['dia-1'])
