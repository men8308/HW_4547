# def sum_numbers(n, y = "hello"):
#     print (y)
#     sum=1
#     for i in range (1, n+1):
#         sum+=1
#     return sum

# a=sum_numbers(5,"Привет")
# print (a)





# def sum_str(*args):
#     res=""
#     for i in args:
#         res+=i
#     return res

# print (sum_str("пр","и","вет"))





# import Modul #импортируем файл с нашей фукцией
# print(Modul.max1(5,8)) #печатаем результат выполнения функции max1, расположенной в файле Modul

# или можно так

# from Modul import max1 # или так from Modul import *
# print(max1(55,8))

# или можно так

import Modul as M
print(M.max1(5,8))
