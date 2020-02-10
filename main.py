# Case - study #6
# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

# This program draws fractals.

# ОСТАЛЬНЫЕ ЗАДАЧИ:
#   1. код ревью + комментарии
#   2. меню программы (выбор фигуры и ее параметров)
#   3. ?локализация

from turtle import *


# Двоичное дерево (спрашивает высоту дерева и величину угла)
def tree():
    pass


# Ветка
def brunch():
    pass


# Кривая Коха, снежинка Коха
def koch():
    pass


def koch_snowflake():
    pass


def minkowski(deep, length):
    if deep == 0:
        forward(length)
    else:
        minkowski(deep - 1, length)
        left(90)
        minkowski(deep - 1, length)
        right(90)
        minkowski(deep - 1, length)
        right(90)
        minkowski(deep - 1, 2 * length)
        left(90)
        minkowski(deep - 1, length)
        left(90)
        minkowski(deep - 1, length)
        right(90)
        minkowski(deep - 1, length)


# Ледяной фрактал 1
def ice_1():
    pass


# Ледяной фрактал 2
def ice_2():
    pass


# Кривая Леви
def levi():
    pass


# Дракон
def dragon():
    pass


def main():
    pass


main()
