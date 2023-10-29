#calcular el numero de placas posibles en guatemala si estan formadas por 3 letras y 3 numeros 

#definimos nuestros valores
def total():
    # son 27 letras por cada posible posicion 
    letras =27*27*27
    # son 10 numeros en cada posible posicion 
    numeros =10*10*10
    #realizamos las opercaiones 
    return letras*numeros

#imprimimos el resultado 
print(total())