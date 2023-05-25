# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# 123 => 6
# 1.23 => 6
# 1,23 => 6

digit = input ("Enter a number")

print (digit)

digit = digit.replace(",","").replace(".","")

print (digit)

res = sum(map(lambda x: int(x), digit)) # Или так res = sum(map(int, digit))
print (res)