import re
#take input 
# ip="hello world"
# #compare format
# regex=r"hello"
# op=re.match(regex,ip)
# print(op)

#only take start value must
ip=" world hello hello hello"
#compare format
regex=r"hello"
op=re.match(regex,ip)
print(op)

#check the search returns first match only
op=re.search(regex,ip)
print(op)

#findall ---stored in list
op=re.findall(regex,ip)
print(op)




