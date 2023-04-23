# def max1(a,b):
#     if a>b:
#         return a
#     return b

#  #Метод Фибоначи
# def Fib(n):
#     if n in [1,2]:
#         return 1
#     return Fib(n-1) +Fib(n-2)

# list_1=[]
# for  i in range (1,19):
#     list_1.append(Fib(i))
# print(list_1)



# метод быстой сортировки

def quick_sort(nums):
    if len(nums)>1:
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        quick_sort(left)
        quick_sort(right)
        i=k=j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1
list1= [5,1,5,8,63,48,4,3,6,8,1]
print(list1)
quick_sort(list1)
print (list1)