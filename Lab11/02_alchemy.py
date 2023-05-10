# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            substance = Storm()
        elif isinstance(other, Fire):
            substance = Lightning()
        elif isinstance(other, Earth):
            substance = Dust()
        else:
            substance = None

        return substance
    
class Water:
    def __init__(self) -> None:
        self.name = 'Вода'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name
    
    def __add__(self, other):
        if isinstance(other, Air):
            substance = Storm()
        elif isinstance(other, Fire):
            substance = Steam()
        elif isinstance(other, Earth):
            substance = Dirt()
        else:
            substance = None
        
        return substance


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            substance = Steam()
        elif isinstance(other, Air):
            substance = Lightning()
        elif isinstance(other, Earth):
            substance = Lava()
        else:
            substance = None

        return substance
    
class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            substance = Dirt()
        elif isinstance(other, Fire):
            substance = Lava()
        elif isinstance(other, Air):
            substance = Dust()
        else:
            substance = None

        return substance
    
class Steam:
    name = 'Пар'

    def __str__(self):
        return self.name
    
class Dirt:
    name = 'Грязь'

    def __str__(self):
        return self.name
    
class Storm:
    name = 'Шторм'

    def __str__(self):
        return self.name

class Lava:
    name = 'Лава'

    def __str__(self):
        return self.name
    
class Lightning:
    name = 'Молния'

    def __str__(self):
        return self.name
    
class Dust:
    name = 'Пыль'

    def __str__(self):
        return self.name
    

print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())



# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
