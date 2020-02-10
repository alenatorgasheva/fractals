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


# Кривая Коха
def koch():
    pass


# Снежинка Коха
def koch_snowflake():
    pass


# Кривая Минковского
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
    print('Выберите фигуру из списка.')
    print('\t1 - двоичное дерево')
    print('\t2 - ветка')
    print('\t3 - кривая Коха')
    print('\t4 - снежинка Коха')
    print('\t5 - ледяной фрактал 1')
    print('\t6 - ледяной фрактал 2')
    print('\t7 - кривая Минковского')
    print('\t8 - кривая Леви')
    print('\t9 - дракон')
    choice = input()

    if choice == '1':
        tree()

    elif choice == '2':
        brunch()

    elif choice == '3':
        koch()

    elif choice == '4':
        koch_snowflake()

    elif choice == '5':
        ice_1()

    elif choice == '6':
        ice_2()

    elif choice == '7':
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        minkowski(deep, length)

    elif choice == '8':
        levi()

    elif choice == '9':
        dragon()


main()
