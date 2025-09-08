# # fibonicci series using recursion
# def recrsive(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return recrsive(n-1)+recrsive(n-2)
# for i in range (5):
#     print(recrsive(i))


# #process 2
# def fib_series(a, b, n):
#     if n > 0:
#         print(a, end=" ")
#         fib_series(b, a+b, n-1)

# # Print first 10 numbers
# fib_series(0, 1, 10)



#2 nested list using recursion
def sum_list(lst):
    total=0
    for val in lst:
        if isinstance (val,list):
            total+=sum_list(val)
        else:
            total+=val
    return total 
x = [1, 2, 3, [1, 2, 3], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]
print(sum_list(x))



#another one
def summ(n):
    sum=0
    for i in n:
        if isinstance(i,list):
            sum+=summ(i)
        else:
            sum+=i
    return sum
x=[1,2,[3,4,5],[1,2,[3,5],6]]
print(summ(x))
            







# #geral way
# x = [1, 2, 3, [1, 2, 3], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]
# total = 0

# for val in x:
#     if isinstance(val, list):
#         for i in val:
#             if isinstance(i, list):
#                 for j in i:
#                     if isinstance(j, list):
#                         for k in j:          
#                             total += k
#                     else:
#                         total += j
#             else:
#                 total += i
#     else:
#         total += val

# print(total)   
