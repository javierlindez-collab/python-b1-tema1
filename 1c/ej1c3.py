"""
Enunciado:

Implementa una función llamada find_max(lst) que encuentre el valor máximo en una
lista de números utilizando recursión. La función debe devolver el valor
máximo de la lista.

Parámetros:
    lst (List): lista de números enteros o flotantes

Ejemplo:
    Entrada:
    numbers_list = [1, 5, 2, 7, 3]
    find_max(numbers_list)

    Salida:
    7


Enunciat:

Implementa una funció anomenada find_max(lst) que trobi el valor màxim en una
llista de números utilitzant recursió. La funció ha de tornar el valor
màxim de la llista.

Paràmetres:
     lst (List): llista de nombres enters o flotants

Exemple:
     Entrada:
     numbers_list = [1, 5, 2, 7, 3]
     fid_max(numbers_list)

     Sortida:
     7

"""


def find_max(lst):
    """ Javier Líndez
        13/11/2026
        Devuelve el máximo de una lista de números utilizando recursión
    """
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] > lst[1]:         # Si el primer número es mayor que el segundo
            t = []                  # Creo una lista temporal
            t.append(lst[0])        # Le añado el primero de la lista lst
            t = t + lst[2:]         # y le añado el resto de la lista lst a partir del 3er número (elimino el segundo número)
            return find_max(t)      # y llamo a la función recursiva con la lista temporal
        else:
            return find_max(lst[1:])    # Si el segundo número es mayor que el primero llamo a la función con la lista desde el segundo número

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# numbers_list = [1, 5, 2, 7, 3]
# print(find_max(numbers_list))
