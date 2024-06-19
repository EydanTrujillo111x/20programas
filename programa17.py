# Solicitar al usuario que introduzca su edad
edad = int(input("Introduce tu edad: "))

# Determinar el tipo de licencia de conducir según la edad
if edad >= 16 and edad <= 17:
    tipo_licencia = "Licencia de menor"
elif edad >= 18 and edad <= 65:
    tipo_licencia = "Licencia de adulto"
elif edad > 65:
    tipo_licencia = "Licencia de adulto mayor"
else:
    tipo_licencia = "No eres elegible para tener una licencia de conducir"

# Mostrar el tipo de licencia de conducir
print(f"A los {edad} años, fuiste seleccionado para tener '{tipo_licencia}'.")