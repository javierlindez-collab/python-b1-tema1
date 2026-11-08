'''
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.
Considerar que 'list_numbers' debe contener valores numéricos enteros mayores
o iguales a '0', en caso contrario se debe mostrar un error tipo 'ValueError'.

El error lo puedes mostrar con la siguiente instrucción:    
raise ValueError("MENSAJE DE ERROR")

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
    Entrada:
    sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

    Salida:
    30

Enunciat:
Crea una funció 'sum_odd_numbers(list_numbers)' que rebi com
paràmetre una llista de nombres positius enters anomenada 'list_numbers'
i torneu la suma dels números imparells trobats a la llista.
Considereu que 'list_numbers' ha de contenir valors numèrics enters majors
o iguals a '0', en cas contrari cal mostrar un error tipus 'ValueError'.

L'error el pots mostrar amb la següent instrucció:
raise ValueError("MISSATGE D'ERROR")

Paràmetres:
- list_numbers: Llista de nombres enters positius.

Exemple:
     Entrada:
     sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

     Sortida:
     30

'''

def sum_odd_numbers(list_numbers):
    """ JAVIER LINDEZ
        8/11/2026
        Calcula la suma de los números impares de una lista de números enteros positivos
    """

    acumula_impares = 0
    for n in list_numbers:
        if not isinstance(n, int):
            raise ValueError("En la lista solo puede haber números enteros")
        elif n < 0:
            raise ValueError("Los números de la lista deben ser enteros y positivos")
        else:
            if(n % 2 != 0):
                acumula_impares += n

    return acumula_impares

    

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))
