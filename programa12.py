salarioB = float(input("Introduce tu salario bruto: "))
if salarioB > 2000:
    impuesto = salarioB * 0.20
    salarioN = salarioB - impuesto
else:
    salarioN = salarioB
print(f"Tu salario neto es {salarioN:}")
