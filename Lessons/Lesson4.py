# def f(x):
#     return x*x*x;
# a=f

# print (f(5));
# print (type(f));
# print (a(5));
# print (type(a));




# def calk1 (a, b):
#     return a + b

# def calk2 (a, b):
#     return a * b

# def math (op, a, b):
#     print (op(a, b))

# math (calk1, 5, 45)




# calk1 = lambda a,b: a*b

# def math (op, a, b):
#     print (op(a, b))

# math (calk1, 5, 45)
# math (lambda a,b: a*b, 5, 45)





# data = [1,2,3,5,8,15,23,38]
# res=list()

# for i in data:
#     if i%2==0 :
#         res.append((i, i**2))

# print (res)


# def select (f, col):
#     return [f(x)for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]

# data = [1,2,3,5,8,15,23,38]
# res =select(int, data)
# print (res)
# res=where(lambda x: x%2==0, res)
# print(res)
# res=list(select(lambda x:(x, x**2), res))
# print(res)


# //////////////////////////////

list_1=[x for x in range(1,20)]
print (list_1)

list_1= list(map(lambda x: x+10, list_1))
print (list_1)