#!/usr/bin/python3
squares = [[00000000, 00000000, 00000000, 00000000],
          [00000000, 00000000, 00000000, 00000000],
          [00000000, 00000000, 00000000, 00000000],
          [00000000, 00000000, 00000000, 00000000]]

squares[2][0] = 2

# print a row, including all cells
def print_row(j):
    print('|  ', end='')
    print(f'{squares[j][0]:08d}', end='')
    print('  |  ', end='')
    print(f'{squares[j][1]:08d}', end='')
    print('  |  ', end='')
    print(f'{squares[j][2]:08d}', end='')
    print('  |  ', end='')
    print(f'{squares[j][3]:08d}', end='')
    print('  |')

def print_square():
    print('+------------+------------+------------+------------+')
    print('|            |            |            |            |')
    print('|            |            |            |            |')
    print_row(0)
    print('|            |            |            |            |')
    print('|            |            |            |            |')
    print('|------------+------------+------------+------------|')
    print('|            |            |            |            |')
    print('|            |            |            |            |')
    print_row(1)
    print('|            |            |            |            |')
    print('|            |            |            |            |')
    print('|------------+------------+------------+------------|')
    print('|            |            |            |            |')
    print('|            |            |            |            |')
    print_row(2)
    print('|            |            |            |            |')
    print('|            |            |            |            |')
    print('|------------+------------+------------+------------|')
    print('|            |            |            |            |')
    print('|            |            |            |            |')
    print_row(3)
    print('|            |            |            |            |')
    print('|            |            |            |            |')
    print('+------------+------------+------------+------------+')

print_square()
