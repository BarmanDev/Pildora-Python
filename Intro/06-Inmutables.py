# Los números booleanos strings y tuplas son inmutables el objeto se va al recolector de basura 
# y se crea uno nuevo

cerveza = "Paularner"
print(id(cerveza))
cerveza = "No insistas cruzcampo no es cerveza"
print(id(cerveza))