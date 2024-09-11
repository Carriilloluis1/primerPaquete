#7 
def calcular_iva(total_ventas :float , iva :float = 21) -> float:
    '''Función que calcula las ventas sin IVA'''
    
    porcentaje_iva = 1 + (iva / 100)
    
    ventas_sin_iva = total_ventas / porcentaje_iva
    
    return ventas_sin_iva

def calcular_retenciones(total_exportaciones :float, retenciones :float = 15) -> float:
    
    '''Esta función calcula las retenciones obtenidas luego de hacer la exportación'''
    
    total_retenciones = 1 - (retenciones / 100)
    
    resultado_exportaciones = total_exportaciones * total_retenciones
    
    return resultado_exportaciones

def calcular_impuestos(ventas_sin_iva, resultado_exportacion) -> float:
    
    '''Esta función el impuesto a las ventas luego de aplicarle el impuesto nacional o internacional'''
    
    resultado_final = ventas_sin_iva + resultado_exportacion
    
    return resultado_final