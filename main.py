# Case - study #6
# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

# This program draws fractals.

from turtle import *


# Двоичное дерево (спрашивает высоту дерева и величину угла)
def tree(size, corner, order):
    if size - size/order > 10:
        forward(size)
        right(corner/2)
        tree(size - size/order, corner, order)
        left(corner)
        tree(size - size/order, corner, order)
        right(corner/2)
        backward(size)


# Кривая Коха
def koch(deep, length):
    if deep == 0:
        forward(length)
    else:
        koch(deep - 1, length / 3)
        left(60)
        koch(deep - 1, length / 3)
        right(120)
        koch(deep - 1, length / 3)
        left(60)
        koch(deep - 1, length / 3)



# Снежинка Коха
def koch_snowflake(deep, length):
    if deep == 0:
        koch(deep, length / 3)
        left(120)
        koch(deep, length / 3)
        left(120)
        koch(deep, length / 3)
        left(120)
    else:
        koch(deep - 1, length / 3)
        left(60)
        koch(deep - 1, length / 3)
        right(120)
        koch(deep - 1, length / 3)
        left(60)
        koch(deep - 1, length / 3)
        right(120)
        koch(deep - 1, length / 3)
        left(60)
        koch(deep - 1, length / 3)
        right(120)
        koch(deep - 1, length / 3)
        left(60)
        koch(deep - 1, length / 3)
        right(120)
        koch(deep - 1, length / 3)
        left(60)
        koch(deep - 1, length / 3)
        right(120)
        koch(deep - 1, length / 3)
        left(60)
        koch(deep - 1, length / 3)



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
def ice_2(deep, length):
    if deep == 0:
        forward(length)
    else:
        ice_2(deep - 1, length)
        left(90)
        ice_2(deep - 1, length / 2)
        left(180)
        ice_2(deep - 1, length / 2)
        left(90)
        ice_2(deep - 1, length)


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
        order = 3
        size = int(input('Длина ствола: '))
        corner = int(input('Угол: '))
        up()
        goto(0, -100)
        left(90)
        down()
        color('green')
        tree(size, corner, order)
        done()

    elif choice == '2':
        color('red')
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
        color('deepskyblue')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-100, 0)
        down()
        koch(deep, length)
        done()

    elif choice == '5':
        color('mediumturquoise')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-100, 0)
        down()
        koch_snowflake(deep, length)
        done()

    elif choice == '6':
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        ice_1(deep, length)


    elif choice == '7':
        ice_1_snowflake()

    elif choice == '8':
        color('midnightblue')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-100, 0)
        down()
        ice_2(deep, length)
        done()


    elif choice == '9':
        ice_2_snowflake()


main()
done()