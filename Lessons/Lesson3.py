# def sum_numbers(n, y = "hello"):
#     print (y)
#     sum=1
#     for i in range (1, n+1):
#         sum+=1
#     return sum

# a=sum_numbers(5,"Привет")
# print (a)





def sum_str(*args):
    res=""
    for i in args:
        res+=i
    return res

print (sum_str("пр","и","вет"))