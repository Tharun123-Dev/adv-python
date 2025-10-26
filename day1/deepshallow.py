
#Shallow Copy (copy.copy())

#Creates a new outer object,

# But does not copy inner objects — they are referenced (shared).

# Changes inside nested lists will affect the original.

#  Deep Copy (copy.deepcopy())

# Creates a completely independent clone —
# both outer and inner objects are copied.

# Changes inside nested lists won’t affect the original.
import copy

# Original list with nested lists
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

print("Before modification:")
print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

# Modify the original list
original[0][0] = 99   # Change inner element
original.append([7, 8, 9])  # Add new sublist

print("\nAfter modification:")
print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

#shallow copy
import copy  

info = {"details": {"name": "nani", "city": "hyd"}}  

x = copy.copy(info)  
y = copy.copy(info)  
x['details']["city"]="wgl"
print(info)
print(x)
print(y)



# #deep copy

info = {"details": {"name": "nani", "city": "hyd"}}  

x = copy.deepcopy(info)  
y = copy.deepcopy(info)  
x['details']["city"]="wgl"
print(info)
print(x)
print(y)


# #example 2
# #shallow copy 

# score_board={"score":{"runs":135,"wickets":4}}
# nani=copy.copy(score_board)
# tharun=copy.copy(score_board)
# nani["score"]["wickets"]="6"
# print(score_board)
# print(nani)
# print(tharun)

# #deep copy

# score_board={"score":{"runs":135,"wickets":4}}
# nani=copy.copy(score_board)
# tharun=copy.copy(score_board)
# nani["score"]["wickets"]="6"
# print(score_board)
# print(nani)
# print(tharun)


#2 sum of the nested list
def nested_sum(x):
    total = 0
    for i in x:
        if isinstance(i, list):
            total += nested_sum(i)  
        else:
            total += i
    return total

x = [1, 2, 3, [1, 2, 3], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]
print("Sum of all numbers:", nested_sum(x))


#3 fibonicci series using recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("Enter number of terms: "))
print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")

#4 without flattening
def nested_sum(x):
    total = 0
    for i in x:
        if isinstance(i, list):    
            total += nested_sum(i)
        else:
            total += i              
    return total

x = [1, 2, 3, [1, 2, 3], 4, 5, 6, [3, 4, 5, [2, 3, 4, [1, 2, 3]]]]

print("Sum of all numbers:", nested_sum(x))
