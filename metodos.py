def salario_real_troste(salario_bruto):
    impuestos = salario_bruto*0.26
    return salario_bruto-impuestos


dinero_real_troste = salario_real_troste(15000) 
print("Trainee de Mecatronica y/o Robotica")
print(dinero_real_troste)
print("==============================")
dinero_real_troste = salario_real_troste(38000)
print("Operaciones Digitales Hubspot y Automatizacion")
print(dinero_real_troste)