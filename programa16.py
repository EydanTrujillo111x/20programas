altura=float(input("ingrese su altura en metros: "))
peso=float(input("ingrese su peso kilogramos:  "))

imc= peso/(altura ** 2) 

if imc < 18.5:
    clasificacion="bajo peso"
elif imc >18.5 and imc <= 24.9:
    clasificacion= "normal"
elif imc >25 and imc <= 29.9:    
    clasificacion="sobrepeso"
else: 
    clasificacion="obesidad"
    
    print(f"su imc es:{imc:2f},lo que indico que tiene {clasificacion}")  
    print("su imc es: + str(round(imc,2 )+, lo que imdique que tiene "+ clasificacion )            