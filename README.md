# VVPD_6
Определяет тип сетевой топологии

# Основные функции программы
# is_full_connected(v, r, links):
Проверяет, является ли сеть полносвязной

:param v: количество вершин
    
:param r: количество ребер
    
:param links: список кортелей (i,j), где (i,j) - наличие связи между i и j. Не используется в функции, добавлена для соблюдения сигнатуры программы
    
:return:
    
True(False) если сеть является(не является) полносвязной
    
![image](https://user-images.githubusercontent.com/96423378/147188057-401e29af-8c67-4fc6-a9c9-9b67b72d3fcc.png)

# connection_type(v, r, links)
Определяет, к какому типу сетей относится заданная сеть

:param v: количество вершин. Не используется в функции, добавлена для соответствия сигнатурам программы

:param r: количество ребер

:param links: список кортелей (i,j), где (i,j) - наличие связи между i и j.

:return:

1, если сеть является шиной

2, если сеть является кольцом

3, если сеть является звездой

-1, если сеть не относится ни к одному из типов

![image](https://user-images.githubusercontent.com/96423378/147186458-b9043a2e-2b4e-4f6a-89a0-67042514dbb6.png)


# Программный код основных функций
```python
def is_full_connected(v, r, links)
    if r == (v * (v - 1)):
        return True
    else:
        return False

def connection_type(v, r, links):
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
```
