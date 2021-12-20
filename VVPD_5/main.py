"""Князьков Денис Алексеевич КИ21-17/1б
Практическая работа №4, 11 вариант"""


def is_full_connected(v, r, links):
    """
    Проверяет, является ли сеть полносвязной
    :param v: количество вершин
    :param r: количество ребер
    :param links: список кортелей (i,j), где (i,j) - наличие связи между i и j.
    :return:
    True(False) если сеть является(не является) полносвязной
    """
    if r == (v * (v - 1)):
        return True
    else:
        return False


def connection_type(v, r, links):
    """
    Определяет, к какому типу сетей относится заданная сеть
    :param v: количество вершин
    :param r: количество ребер
    :param links: список кортелей (i,j), где (i,j) - наличие связи между i и j.
    :return:
    1, если сеть является шиной
    2, если сеть является кольцом
    3, если сеть является звездой
    -1, если сеть не относится ни к одному из типов
    """
    dict_of_links = {}
    for x in links:
        if x[0] in dict_of_links:
            dict_of_links[x[0]].add(x[1])
        else:
            dict_of_links[x[0]] = {x[1]}
        if x[1] in dict_of_links:
            dict_of_links[x[1]].add(x[0])
        else:
            dict_of_links[x[1]] = {x[0]}
    flag = 0
    for x in dict_of_links:
        if len(dict_of_links[x]) == 1:
            continue
        elif len(dict_of_links[x]) == r:
            flag = 1
        else:
            break
    if flag:
        return 3
    counter = 0
    for x in dict_of_links:
        if len(dict_of_links[x]) == 1:
            counter += 1
        elif len(dict_of_links[x]) == 2:
            continue
        else:
            return -1
    else:
        if counter == 0:
            return 2
        elif counter == 2:
            return 1



print("1 - Шина, 2 - Кольцо, 3 - Звезда, -1 - Не относится ни к одному из данных типов ")
first = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2),
         (4, 3)]  # Сеть является полносвязной
print(is_full_connected(4, 12, first))
print(connection_type(4, 12, first))
second = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)]  # Сеть является неполносвязной, кольцо
print(is_full_connected(5, 5, second))
print(connection_type(5, 5, second))
third = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]  # Сеть является неполносвязной, шина
print(is_full_connected(6, 5, third))
print(connection_type(6, 5, third))
fourth = [(1, 2), (1, 3), (1, 4), (1, 5)]  # Сеть является неполносвязной, звезда
print(is_full_connected(5, 4, fourth))
print(connection_type(5, 4, fourth))
fifth = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3)]  # Сеть является неполносвязной и не относится ни к одному из типов
print(is_full_connected(4, 5, fifth))
print(connection_type(4, 5, fifth))
