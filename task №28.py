# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a, b):

    if a == 0:
        return b
    return sum(a-1, b+1)


val_a = int(input('Enter number a:  '))
val_b = int(input('Enter number b:  '))

if val_a < 0 or val_b < 0:
    print('You entered a negative number!')
else:
    print(f'Sum of numbers = {sum(val_a, val_b)}')
