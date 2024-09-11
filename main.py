#Main del ejercicio 7

# from paquetes import ejercicio7

# resultado_sin_iva = ejercicio7.calcular_iva(100)
# print(resultado_sin_iva)

# resultado_exportaciones = ejercicio7.calcular_retenciones(500)
# print(resultado_exportaciones)

# total_impuestos = ejercicio7.calcular_impuestos(resultado_sin_iva,resultado_exportaciones)
# print(f'Los impuestos son {total_impuestos}')

#Main del ejercicio 8
from paquetes import ejercicio8
salario_total = ejercicio8.calcularSalario(20,1)
productividad_total = ejercicio8.calcularProductividad(25,20)
total_datos = ejercicio8.informarDatos("Jose", 25, salario_total, productividad_total)

print(total_datos)