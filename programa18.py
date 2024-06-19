# Solicitar un número al usuario
numero = int(input("Ingrese un número: "))

# Determinar la divisibilidad
if numero % 3 == 0 and numero % 5 == 0:
    resultado = "El número es divisible por 3 y por 5."
elif numero % 3 == 0:
    resultado = "El número es divisible por 3."
elif numero % 5 == 0:
    resultado = "El número es divisible por 5."
else:
    resultado = "El número no es divisible ni por 3 ni por 5."

# Mostrar el resultado
print(resultado)
