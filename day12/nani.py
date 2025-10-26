# n="ganesh"
# l=" "
# for i in n:
#     if i in ["a","e"]:
#           m = chr(ord(i) + 1)
#           l+=m
#     else:
#         l+=i
# print(l)

# #adding
# n = "zaxman"
# d = 2
# m = " "
# for i in n:
#     if i == "z":
#         m += chr(96  + d)
#     else:
#         m += chr(ord(i) + d)
# print(m)


#occarances solve s
s = "aaabbccdab"
result = ""
count = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1


result += s[-1] + str(count)

print(result)


#palindrom
a = "malayalam"
pal = 0
for i in range(len(a)):
    for j in range(i + 1, len(a) + 1):
        temp = a[i:j]
        if temp == temp[::-1] and len(temp) > 1:
            pal += 1
print(pal)
        



    

