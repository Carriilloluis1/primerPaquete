#8.
def calcularSalario(horas_trabajadas : float, antiguedad : int) -> float:
    
    '''La función calcula el salario total de un empleado'''
    salario = horas_trabajadas * 10 
    
    #Calculamos bonificación por antigüedad
    porcentaje_antiguedad = ((3 * salario / 100)) * antiguedad
    
    salario_total = salario + porcentaje_antiguedad
    
    return salario_total

def calcularProductividad(total_artefactos : int, horas_trabajadas : float) -> float:
    '''La función determina la productividad del empleado'''
    
    productividad_total = total_artefactos / horas_trabajadas
    
    return productividad_total 

def informarDatos(nombre_empleado, edad_empleado, salario_total, productividad_total):
    
    '''Informa por pantalla los datos del empleado'''
    
    return f'''El Empleado es: {nombre_empleado} 
Su edad es: {edad_empleado} 
El sueldo es: {salario_total} 
La productividad es {productividad_total}'''