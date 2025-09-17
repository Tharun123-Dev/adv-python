from functools import reduce

#1 sum of elements
nums=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,nums)
print(sum)

#2 product of elements
nums=[1,2,3,4,5]
sum=reduce(lambda x,y:x*y,nums)
print(sum)

#3miminum
#3 min of elements
nums=[1,2,3,4,5]
min=reduce(lambda x,y:x if x<y else y,nums)
print(min)

#4 max of elements
nums=[1,2,3,4,5]
min=reduce(lambda x,y:x if x>y else y,nums)
print(min)

#5 concating the strings
s=["i","love"," india"]
op=reduce(lambda x,y:x+" "+y,s)
print(op)

#6.	Flatten a List of Lists
#lists = [[1, 2], [3, 4], [5, 6]]
#flat = reduce(lambda a, b: a + b, lists)
#print(flat) 
lists = [[1, 2], [3, 4], [5, 6]] 
flat = reduce(lambda a, b: a + b, lists)
print(flat)

#7 Factorial Calculation
n = 5
fact = reduce(lambda a, b: a * b, range(1, n+1))
print(fact)  

#7.Convert Digits List → Number
digits = [1, 2, 3, 4]
num = reduce(lambda a, b: a * 10 + b, digits)
print(num)  # 1234
#8.Custom Aggregations Example → Longest word:
words = ["apple", "banana", "cherry", "watermelon"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest)  

#6.	Greatest Common Divisor (GCD)
import math
nums = [48, 64, 80]
gcd_val = reduce(math.gcd, nums)
print(gcd_val)  












