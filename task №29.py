# Задача №29. Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)

number = maxNumber = int(input("Введите цифру: "))


while (number != 0):
if (number > maxNumber):
maxNumber = number
# значение тру if (условие) else значение елзе
#maxNumber = number if number > maxNumber else maxNumber
number = int(input("Введите цифру: "))

print(f"Максимальный элемент: {maxNumber}")