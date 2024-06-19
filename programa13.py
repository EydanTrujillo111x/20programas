año =int(input("Introduce el año: "))
if año % 100 == 0:
    print(f"{año} es el primer año de un siglo")
else:
    print(f"{año} no es el primer año de un siglo")