

def arr(n):
    large=n[0]
    for i in n:
        if i>large:
            large=i
            second=large
        elif i!=large :
         print(second)
         break


x=[2,3,6,4,7]
arr(x)



s = "HeLLoWoRLd123"

upper = ""
lower = ""

for ch in s:
    if ch.isupper():
        upper += ch
    else:
        lower += ch

result = upper + lower
print(result)   # HLLWRLdeo123


#######
n = 5  # height of the top half

# Upper part
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

# Lower part
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))




# def fun(stri):
#  strr=" "
#  for i in stri:
#     if str(i).upper():
#         strr=strr+i
#         print(strr)
    
    
#     else:

#      strr=strr+i
#      print(strr)
# fun("HaPppy")




 


# def fun(stri):
#  strr=" "
#  for i in stri:
#     if str(i).upper():
#         strr=strr+i
#     print(strr)
#  else:

#     strr=strr+i
#     print(strr)

     
# fun("moveMENT")

# def fun(stri):
#  strr=" "
#  for i in stri:
#     if i.isupper():
#         strr=strr+i
#         print(strr)
#     else:
#         strr=strr+i
#         print(strr)
# fun("shrtCAKE")


# # # #3
# row=5
# for i in range(1,row+5,2):
#    print(" "*(row-i-1)+"*"*i)



# text = "hello world"

# # Capitalize first letter without isupper()# result = text[0].upper() + text[1:]

# print(result)  # Output: Hello world

for in range(1,)
















    
    

