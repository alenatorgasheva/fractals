# Case - study #6
# This program draws fractals.

# Developers : Daniel A.         (40%),
#              Zemtseva A.       (37%),
#              Torgasheva A.     (40%).

from turtle import *


def branch(length, deep):
    '''
    Function, drawing a branch.
    :param length: a length of the initial line
    :param deep: a recursion depth
    :return: None
    '''
    if deep == 0:
        left(180)
        return

    for i in range(1, deep + 1):
        forward(length / (deep + 1))
        left(45)
        branch(((length / (deep + 1)) / 2) * (deep - i), deep - i)
        left(90)
        branch(((length / (deep + 1)) / 2) * (deep - i), deep - i)
        right(135)

    forward(length / (deep + 1))
    left(180)
    forward(length)


def tree(length, corner):
    '''
    Function, drawing a binary tree.
    :param length: a length of the initial line
    :param corner: a corner between the branches of tree
    :return: None
    '''
    if length - length / 3 > 10:
        forward(length)
        right(corner / 2)
        tree(length - length / 3, corner)
        left(corner)
        tree(length - length / 3, corner)
        right(corner / 2)
        backward(length)
    else:
        return


def koch(deep, length):
    '''
    Function, drawing the Koch's curve.
    :param deep: a recursion depth
    :param length: a length of the initial line
    :return: None
    '''
    if deep == 0:
        forward(length)
    else:
        koch(deep - 1, length / 2)
        left(60)
        koch(deep - 1, length / 2)
        right(120)
        koch(deep - 1, length / 2)
        left(60)
        koch(deep - 1, length / 2)


def koch_snowflake(deep, length):
    '''
    Function, drawing a Koch's snowflake.
    :param deep: a recursion depth
    :param length: a length of the initial line
    :return: None
    '''
    koch(deep, length / 3)
    right(120)
    koch(deep, length / 3)
    right(120)
    koch(deep, length / 3)
    right(120)


def minkowski(deep, length):
    '''
    Function, drawing a Minkowsky's curve.
    :param deep: a recursion depth
    :param length: a length of the initial line
    :return: None
    '''
    if deep == 0:
        forward(length)
    else:
        minkowski(deep - 1, length / 2)
        left(90)
        minkowski(deep - 1, length / 2)
        right(90)
        minkowski(deep - 1, length / 2)
        right(90)
        minkowski(deep - 1, length)
        left(90)
        minkowski(deep - 1, length / 2)
        left(90)
        minkowski(deep - 1, length / 2)
        right(90)
        minkowski(deep - 1, length / 2)


def ice_1(deep, length):
    '''
    Function, drawing an ice fractal number 1.
    :param deep: a recursion depth
    :param length: a length of the initial line
    :return: None
    '''
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


def ice_1_snowflake_1(deep, length):
    '''
    Function, drawing a snowflake number 1 consisting of ice fractals number 1.
    :param deep: a recursion depth
    :param length: a length of the initial line
    :return: None
    '''
    right(180)
    ice_1(deep, length)
    right(180)
    ice_1(deep, length)
    for _ in range(5):
        left(120)
        ice_1(deep, length)
        right(180)
        ice_1(deep, length)


def ice_1_snowflake_2(deep, length):
    '''
    Function, drawing a snowflake number 2 consisting of ice fractals number 1.
    :param deep: a recursion depth
    :param length: a length of the initial line
    :return: None
    '''
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
    left(180)


def ice_2(deep, length):
    '''
    Function, drawing an ice fractal number 2.
    :param deep: a recursion depth
    :param length: a length of the initial line
    :return: None
    '''
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


def ice_2_snowflake(deep, length):
    ice_2(deep, length)
    ice_2(deep, length)
    right(180)
    ice_2(deep, length)
    right(45)
    ice_2(deep, length)
    right(180)
    ice_2(deep, length)
    ice_2(deep, length)
    right(180)
    ice_2(deep, length)
    right(90)
    ice_2(deep, length)
    right(180)
    ice_2(deep, length)
    ice_2(deep, length)
    right(180)
    ice_2(deep, length)
    left(45)
    ice_2(deep, length)
    right(180)
    ice_2(deep, length)
    ice_2(deep, length)
    right(180)
    ice_2(deep, length)
    left(90)
    ice_2(deep, length)


def ice_2_snowflake_2(deep, length):
    ice_2(deep, length)
    right(90)
    ice_2(deep, length)
    right(90)
    ice_2(deep, length)
    right(90)
    ice_2(deep, length)
    right(180)
    ice_2(deep, length)
    left(90)
    ice_2(deep, length)
    left(90)
    ice_2(deep, length)
    left(90)
    ice_2(deep, length)


def levi(deep, length):
    '''
    Function, drawing a Levi's curve.
    :param deep: a recursion depth
    :param length: a length of the initial line
    :return: None
    '''
    if deep == 0:
        forward(length)
    else:
        left(45)
        levi(deep - 1, length / 1.5)
        right(90)
        levi(deep - 1, length / 1.5)
        left(45)


def main():
    # Choosing the language
    language = input('Choose your language:\n1. English\n2. Russian\n').lower()
    while True:
        if language == 'english' or language == 'eng' or \
                language == 'e' or language == '1':
            import lc_eng as lc
            break
        elif language == 'russian' or language == 'rus' or \
                language == 'r' or language == '2':
            import lc_rus as lc
            break
        language = input('Please, choose language from proposed: ')

    while True:
        # Main menu
        print('-' * 50)
        print(lc.TXT_TASK)
        print(lc.TXT_CHOICE)
        choice = input()
        print('-' * 50)

        speed(9)

        if choice == '1':
            length = int(input(lc.TXT_TREE_LENGTH))
            angle = int(input(lc.TXT_TREE_ANGLE))
            up()
            goto(0, -(length * 1.5))
            left(90)
            down()
            color('green')
            tree(length, angle)
            right(90)

        elif choice == '2':
            length = int(input(lc.TXT_LENGTH))
            n = int(input(lc.TXT_DEEP))
            left(90)
            color('sienna')
            up()
            goto(0, -length / 3)
            down()
            branch(length, n)
            left(90)

        elif choice == '3':
            color('red')
            order = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length, 0)
            down()
            levi(order, length)

        elif choice == '4':
            color('deeppink')
            deep = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length * 2, 0)
            down()
            minkowski(deep, length)

        elif choice == '5':
            color('aqua')
            deep = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length * 2, 0)
            down()
            koch(deep, length)

        elif choice == '6':
            color('aqua')
            deep = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length / 2, length / 2)
            down()
            koch_snowflake(deep, length)

        elif choice == '7':
            color('royalblue')
            deep = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length * 2 ** (deep - 1), 0)
            down()
            ice_1(deep, length)

        elif choice == '8':
            color('royalblue')
            deep = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length, 0)
            down()
            ice_1_snowflake_1(deep, length)
            right(60)

        elif choice == '9':
            color('royalblue')
            deep = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length, length)
            down()
            ice_1_snowflake_2(deep, length)

        elif choice == '10':
            color('indigo')
            deep = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length * 2 ** (deep - 1), 0)
            down()
            ice_2(deep, length)

        elif choice == '11':
            color('indigo')
            deep = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length * 2, 0)
            down()
            ice_2_snowflake(deep, length)
            right(180)

        elif choice == '12':
            color('indigo')
            deep = int(input(lc.TXT_DEEP))
            length = int(input(lc.TXT_LENGTH))
            up()
            goto(-length * 2, length * 2)
            down()
            ice_2_snowflake_2(deep, length)
            right(180)

        else:
            print('-' * 50)
            print(lc.TXT_ERROR)

        print('-' * 50)
        print(lc.TXT_AGAIN)
        choice = input()
        if choice == '1':
            clear()
        elif choice == '2':
            exit()


main()
done()
