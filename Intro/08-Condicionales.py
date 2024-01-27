# else if
edad = 12

if edad < 18:
    print("Puedes beber cruzcampo")
else:
    print("Puedes beber cerveza")

# Ifs anidados 
edad = 200
if edad >= 0 and edad <=12:
    print("eres un nenin")
elif edad <= 13 and edad <= 17:
    print("Eres adolescente")
elif edad >=19 and edad <=100:
    print("Eres un adulto")
elif edad >= 101:
    print("Cuidate :)")

## Operador OR se cumple una condición

edad = 25

if edad < 18 or edad > 65:
    print("Tienes descuento bonobus")
else:
    print("Pasa por caja")

# Operaador AND se cumple las dos condiciones
cervezas = 200
invitados = 10

if cervezas > 0 and invitados > 0:
    print("Estamos a viernes y el cuepo lo sabe")