#determine si un numero es primo
nu=int(input("ingrese el numero:"))

x=1
c=0

while x <= nu:
    if nu % x == 0:
     c=c+1
     x=x+1
    
    if c == 2:
     print(f"El número {nu} es primo")
    else:
     print(f"El número {nu} no es primo")