
import re

# #only take start value must
# ip=" world hello hello hello"
# #compare format
# regex=r"hello"
# op=re.match(regex,ip)
# print(op)

# #check the search returns first match only
# op=re.search(regex,ip)
# print(op)

# #findall ---stored in list
# op=re.findall(regex,ip)
# print(op)


# #checking start with hdfc and ends with numbers

# regex=r"^hdfc\d+$"
# op=re.search(regex,"hdfc123")
# if op:
#     print("valid")
# else:
#     print("invalid")

# #checking atleast one number 

# regex=r"[a-zA-Z3-7]"
# op=re.search(regex,"aA85")
# if op:
#     print("valid")
# else:
#     print("invalid") #valid

# #2
# regex=r"[a-zA-Z3-7]"
# op=re.search(regex,"1")
# if op:
#     print("valid")
# else:
#     print("invalid") #in valid

# #()---using paranthesis
# regex=r"(a-f)" #using "a"."-",""
# op=re.search(regex,"cde")
# if op:
#     print("valid")
# else:
#     print("invalid") #invalid


# #after using these three valid only contain a grouping word (a-f) only grouping of this
# regex=r"(a-f)" #using "a"."-",""
# op=re.search(regex,"oka-faa")
# if op:
#     print("valid")
# else:
#     print("invalid") #valid


# # {}===length of elements {5}===fixed 5 {5,}===more than 5, {,5}---->less than five
# regex=r"{}"
# op=re.search(regex,"cde")
# if op:
#     print("valid")
# else:
#     print("invalid")

#check a valid phonenumbers of indian
#starts with +91 and 10numbers
# regex=r"[6-9]{1}[0-9]{1}"
# op=re.search(regex,"9381836355")
# if op:
#     print("valid")
# else:
#     print("invalid")


#2
# regex=r"[6-9]{1}[0-9]{1}"
# op=re.search(regex,"9381836355")
# if op:
#     print("valid")
# else:
#     print("invalid")

#valid mobile number

# regex = r'^\+91[0-9]{10}$'

# phone = input("Enter phone number: ")

# if re.fullmatch(regex, phone):
#     print("Valid Indian Phone Number")
# else:
#     print("Invalid Phone Number")

#3
# regex = r'^(\+91)\s[6-9]{1}[0-9]{9}$'

# phone = input("Enter phone number: ")

# if re.fullmatch(regex, phone):
#     print("Valid Indian Phone Number")
# else:
#     print("Invalid Phone Number")


#pincode checking validate
regex=r"^[1-9]{1}[0-9]{5}$"
op=re.search(regex,"123564")
if op:
    print("valid")
else:
    print("invalid")

#



