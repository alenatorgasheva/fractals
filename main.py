# Case - study #6
# Developers : Daniel A.         (%),
#              Zemtseva A.       (%),
#              Torgasheva A.     (%).

# This program draws fractals.

from turtle import *


# Ветка
def branch(size, n):
    if n == 0:
        left(180)
        return

    for i in range(1, n + 1):
        forward(size / (n + 1))
        left(45)
        branch(((size / (n + 1)) / 2) * (n - i), n - i)
        left(90)
        branch(((size / (n + 1)) / 2) * (n - i), n - i)
        right(135)

    forward(size / (n + 1))
    left(180)
    forward(size)


# Двоичное дерево
def tree(size, corner):
    if size - size / 3 > 10:
        forward(size)
        right(corner / 2)
        tree(size - size / 3, corner)
        left(corner)
        tree(size - size / 3, corner)
        right(corner / 2)
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
        koch_snowflake(deep - 1, length / 3)
        left(60)
        koch_snowflake(deep - 1, length / 3)
        right(120)
        koch_snowflake(deep - 1, length / 3)
        left(60)
        koch_snowflake(deep - 1, length / 3)
        right(120)
        koch_snowflake(deep - 1, length / 3)
        left(60)
        koch_snowflake(deep - 1, length / 3)
        right(120)
        koch_snowflake(deep - 1, length / 3)
        left(60)
        koch_snowflake(deep - 1, length / 3)
        right(120)
        koch_snowflake(deep - 1, length / 3)
        left(60)
        koch_snowflake(deep - 1, length / 3)
        right(120)
        koch_snowflake(deep - 1, length / 3)
        left(60)
        koch_snowflake(deep - 1, length / 3)


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


# Ледяной фрактал 1, снежинка (1)
def ice_1_snowflake_1(deep, length):
    right(180)
    ice_1(deep, length)
    right(180)
    ice_1(deep, length)
    for _ in range(5):
        left(120)
        ice_1(deep, length)
        right(180)
        ice_1(deep, length)


# Ледяной фрактал 1, снежинка (2)
def ice_1_snowflake_2(deep, length):
    ice_1(deep, length)
    right(120)
    ice_1(deep, length)
    right(120)
    ice_1(deep, length)
    right(180)
    ice_1(deep, length)
    left(120)
    ice_1(deep, length)
    left(120)
    ice_1(deep, length)


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


# Ледяной фрактал 2, снежинка (1)
def snowflake_2(deep, length):
    if deep == 0:
        forward(length)
    else:
        snowflake_2(deep - 1, length)
        left(90)
        snowflake_2(deep - 1, length / 2)
        left(180)
        snowflake_2(deep - 1, length / 2)
        left(90)
        snowflake_2(deep - 1, length)


def ice_2_snowflake(deep, length):
    snowflake_2(deep, length)
    snowflake_2(deep, length)
    right(180)
    snowflake_2(deep, length)
    right(45)
    snowflake_2(deep, length)
    right(180)
    snowflake_2(deep, length)
    snowflake_2(deep, length)
    right(180)
    snowflake_2(deep, length)
    right(90)
    snowflake_2(deep, length)
    right(180)
    snowflake_2(deep, length)
    snowflake_2(deep, length)
    right(180)
    snowflake_2(deep, length)
    left(45)
    snowflake_2(deep, length)
    right(180)
    snowflake_2(deep, length)
    snowflake_2(deep, length)
    right(180)
    snowflake_2(deep, length)
    left(90)
    snowflake_2(deep, length)


# Ледяной фрактал 2, снежинка (2)
def snowflake_2_2(deep, length):
    if deep == 0:
        forward(length)
    else:
        snowflake_2_2(deep - 1, length)
        left(90)
        snowflake_2_2(deep - 1, length / 2)
        left(180)
        snowflake_2_2(deep - 1, length / 2)
        left(90)
        snowflake_2(deep - 1, length)


def ice_2_snowflake_2(deep, length):
    snowflake_2_2(deep, length)
    right(90)
    snowflake_2_2(deep, length)
    right(90)
    snowflake_2_2(deep, length)
    right(90)
    snowflake_2_2(deep, length)
    right(180)
    snowflake_2_2(deep, length)
    left(90)
    snowflake_2_2(deep, length)
    left(90)
    snowflake_2_2(deep, length)
    left(90)
    snowflake_2_2(deep, length)


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
    print('\t2 - ветка')
    print('\t3 - кривая Леви')
    print('\t4 - кривая Минковского')
    print('\t5 - кривая Коха')
    print('\t6 - снежинка Коха')
    print('\t7 - ледяной фрактал 1')
    print('\t8 - ледяной фрактал 1, снежинка (1)')
    print('\t9 - ледяной фрактал 1, снежинка (2)')
    print('\t10 - ледяной фрактал 2')
    print('\t11 - ледяной фрактал 2, снежинка (1)')
    print('\t12 - ледяной фрактал 2, снежинка (2)')
    choice = input()
    print('-' * 50)

    speed(100)

    if choice == '1':
        size = int(input('Длина ствола: '))
        corner = int(input('Угол: '))
        up()
        goto(0, -size*1.5)
        left(90)
        down()
        color('green')
        tree(size, corner)

    elif choice == '2':
        size = int(input('Длина: '))
        n = int(input('Глубина: '))
        left(90)
        color('sienna')
        up()
        goto(0, -size / 3)
        down()
        branch(size, n)

    elif choice == '3':
        color('salmon')
        order = int(input('Глубина: '))
        size = int(input('Длина стороны: '))
        up()
        goto(-100, 0)
        down()
        levi(order, size)

    elif choice == '4':
        color('teal')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        minkowski(deep, length)

    elif choice == '5':
        color('deepskyblue')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-100, 0)
        down()
        koch(deep, length)

    elif choice == '6':
        color('mediumturquoise')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-100, 0)
        down()
        koch_snowflake(deep, length)

    elif choice == '7':
        color('royalblue')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-length / 2, 0)
        down()
        ice_1(deep, length)

    elif choice == '8':
        color('midnightblue')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-length, 0)
        down()
        ice_1_snowflake(deep, length)

    elif choice == '9':
        color('midnightblue')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-length, length)
        down()
        ice_1_snowflake_2(deep, length)

    elif choice == '10':
        color('royalblue')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-100, 0)
        down()
        ice_2(deep, length)

    elif choice == '11':
        color('midnightblue')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-250, 50)
        down()
        ice_2_snowflake(deep, length)

    elif choice == '12':
        color('midnightblue')
        deep = int(input('Глубина: '))
        length = int(input('Длина стороны: '))
        up()
        goto(-250, 50)
        down()
        ice_2_snowflake_2(deep, length)


main()
done()
