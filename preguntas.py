"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv


def load_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file,delimiter="\t")
        
        data = list(reader)
    return data

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = load_data(r"data.csv")
    sum_second_column = sum(int(row[1]) for row in data)
    
    return sum_second_column




def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = load_data(r"data.csv")
    count_dict = {}
    for row in data:
        count_dict[row[0]] = count_dict.get(row[0], 0) + 1

    sorted_count = sorted(count_dict.items())

    return sorted_count



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = load_data(r"data.csv")
    sums = {}
    for row in data:
        letter = row[0]
        value = int(row[1])
        if letter in sums:
            sums[letter] += value
        else:
            sums[letter] = value
    sorted_sums = sorted(sums.items())
    return sorted_sums


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = load_data(r"data.csv")
    count_dict = {}
    for row in data:
        count_dict[row[2][5:7]] = count_dict.get(row[2][5:7], 0) + 1

    sorted_count = sorted(count_dict.items())
    return sorted_count


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = load_data(r"data.csv")
    sums = {}
    for row in data:
        letter = row[0]
        value = int(row[1])
        if letter in sums:
            if sums[letter][0] <= value:
                sums[letter][0] = value
            if sums[letter][1] > value:
                sums[letter][1] = value
        else:
            sums[letter] = [value, value]
    
    sorted_count = sorted(sums.items())

    out = [(letter, *values) for letter, values in sorted_count] 
    return  out


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = load_data(r"data.csv")
    list_explode = {}
    for row in data:
        for item in row[4].split(","):
            key, value = item.split(":")
            if key in list_explode:
                list_explode[key].append(int(value))
            else:
                list_explode[key] = [int(value)]

    out = []
    for key, values in list_explode.items():
        out.append((key, min(values), max(values)))

    sorted_out = sorted(out)
    return sorted_out



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = load_data(r"data.csv")
    out = {}
    for row in data:
        colum1 = int(row[1])
        column0 = row[0]

        if colum1 in out:
            out[colum1].append(column0)
        else:
            out[colum1] = [column0]

    sorted_out = sorted(out.items())
    return sorted_out



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    input_data = pregunta_07()

    out = [(key, sorted(list(set(values)))) for key, values in input_data]

    return out



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = load_data(r"data.csv")
    list_explode = {}
    for row in data:
        for item in row[4].split(","):
            key, _ = item.split(":")
            list_explode[key] = list_explode.get(key, 0) + 1
 
    sorted_out = dict(sorted(list_explode.items()))
    return sorted_out


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    data = load_data(r"data.csv")
    list_explode = []
    for row in data:
        list_explode.append(
            (row[0], len(row[3].split(",")), len(row[4].split(","))))

    return list_explode


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """

    data = load_data(r"data.csv")
    list_explode = {}
    for row in data:
        for item in row[3].split(","):
            
            list_explode[item] = list_explode.get(item, 0) + int(row[1])
    
    sorted_out = sorted(list_explode.items())
    return dict(sorted_out)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = load_data(r"data.csv")
    list_explode = {}
    for row in data:
        sum_row = []
        for item in row[4].split(","):
            _, value = item.split(":")
            sum_row.append(int(value))

        list_explode[row[0]] = list_explode.get(row[0], 0) + sum(sum_row)
    
    sorted_out = dict(sorted(list_explode.items()))

    return sorted_out

#print(pregunta_12())