'''
Enunciado:
Implementar la función 'results(list_numbers)' que reciba como parámetro una
lista que contiene números enteros y decimales llamada 'list_numbers', se pide
calcular el promedio y la desviación estándar mediante la
librería "Numpy" de todos los números dentro de la lista.

Cada resultado se debe imprimir en pantalla con su respectivo nombre 
'Average: {value}' y 'Standard deviation: {value}', dichos resultados deben
estar redondeados a 2 decimales. 

Los resultados también han de ser devueltos por la función.

Puedes consultar la referencia de la librería 'Numpy' en el siguiente enlace:
https://numpy.org/doc/stable/reference/index.html#reference

En concreto, te recomendamos que consultes:
* https://numpy.org/doc/stable/reference/generated/numpy.mean.html
* https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std

Parámetro:
- list_numbers: Lista de números enteros y decimales.

Ejemplo:
    Entrada:
    [1, 2, 10, -5, 0, 9.55, 74.825, 55, 8, 42]
    
    Salida:
    Average: 19.74
    Standard deviation: 26.03

Enunciat:

Implementar la funció 'results(list_numbers)' que rebi com a paràmetre una
llista que conté nombres enters i decimals anomenada 'list_numbers', es demana
calcular la mitjana i la desviació estàndard mitjançant la
llibreria "Numpy" de tots els números dins de la llista.

Cada resultat s'ha d'imprimir en pantalla amb el nom respectiu
'Average: {value}' i 'Standard deviation: {value}', aquests resultats deuen
estar arrodonits a 2 decimals.

Els resultats també han de ser retornats per la funció.

Pots consultar la referència de la llibreria 'Numpy' en el següent enllaç:
https://numpy.org/doc/stable/reference/index.html#reference

En concret, et recomanem que consultis:
* https://numpy.org/doc/stable/reference/generated/numpy.mean.html
* https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std

Paràmetre:
- list_numbers: Llista de nombres enters i decimals.

Exemple:
     Entrada:
     [1, 2, 10, -5, 0, 9.55, 74.825, 55, 8, 42]
    
     Sortida:
     Average: 19.74
     Standard deviation: 26.03
'''


import numpy as np

def results(list_numbers):
    """ Javier Líndez
        11/11/2026
        Promedio y Desviación estándar con la librería Numpy
    """
    # Convertir la lista en array
    array_numbers = np.array(list_numbers)

    # Promedio (Average)
    average = round(np.mean(array_numbers), 2)

    # Desviación estándar (Standard deviation)
    stand = round(np.std(array_numbers), 2)

    print(f"Average: {average:.2f}")
    print(f"Standard deviation: {stand:.2f}")

    return(average, stand)


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# results([1, 2, 10, -5, 0, 9.55, 74.825, 55, 8, 42])
