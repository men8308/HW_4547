# Задача 26:  Посчитать N! и треугольное число (сумма чисел от 1 до N)
# для числа N через рекурсию и без циклов

def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n


def triang(n):
    if n == 1:
        return 1
    return triang(n - 1) + n


num = int(input('Enter number n: '))
print(f'factorial of the number {num} = {fact(num)}')
print(f'a triangular number is a number {num} = {triang(num)}')