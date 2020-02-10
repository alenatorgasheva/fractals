# Case - study #6
# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

# This program draws fractals.

from turtle import *


# Двоичное дерево (спрашивает высоту дерева и величину угла)
def tree():
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
def ice_1(deep, length):
    if deep == 0:
        forward(length)
    else:
        ice_1(deep - 1, length)
        left(120)
        ice_1(deep - 1, length / 2)
        left(180)
        ice_1(deep - 1, length / 2)
        left(120)
        ice_1(deep - 1, length / 2)
        left(180)
        ice_1(deep - 1, length / 2)
        left(120)
        ice_1(deep - 1, length)


# Ледяной фрактал 1, снежинка
def ice_1_snowflake():
    pass


# Ледяной фрактал 2
def ice_2():
    pass


# Ледяной фрактал 2, снежинка
def ice_2_snowflake():
    pass


# Кривая Леви
def levi(order, size):
    if order == 0:
        forward(size)
    else:
        left(45)
        levi(order - 1, size / 1.5)
        right(90)
        levi(order - 1, size / 1.5)
        left(45)


def main():
    print('Выберите фигуру из списка.')
    print('\t1 - двоичное дерево')
    print('\t2 - кривая Леви')
    print('\t3 - кривая Минковского')
    print('\t4 - кривая Коха')
    print('\t5 - снежинка Коха')
    print('\t6 - ледяной фрактал 1')
    print('\t7 - ледяной фрактал 1, снежинка')
    print('\t8 - ледяной фрактал 2')
    print('\t9 - ледяной фрактал 2, снежинка')
    choice = input()

    if choice == '1':
        tree()

    elif choice == '2':
        order = int(input('Глубина: '))
        size = int(input('Длина стороны: '))
        up()
        goto(-100, 0)
        down()
        levi(order, size)
        done()

    elif choice == '3':
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        minkowski(deep, length)

    elif choice == '4':
        koch()

    elif choice == '5':
        koch_snowflake()

    elif choice == '6':
        ice_1()

    elif choice == '7':
        ice_1_snowflake()

    elif choice == '8':
        ice_2()

    elif choice == '9':
        ice_2_snowflake()


main()
