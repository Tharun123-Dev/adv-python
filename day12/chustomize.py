#usename should contain 3 l3tters and start with p and end with t anywhere in the string then it will allow other


import re
#pancard checking first five characters and then numbers four digits and last one must and should last one--one character
# regex=r"^[A-z]{5}+[0-9]{4}+[A-Z]{1}$"

# op=re.search(regex,"THARU1234R")
# if op:
#     print("valid")
# else:
#     print("not")

#method 2
# import re

# regex = r"[A-Z]{5}[0-9]{4}[A-Z]"

# op = re.fullmatch(regex, "THARU1234R")
# if op:
#     print("valid")
# else:
#     print("not")


# regex=r"p.t"
# op=re.search(regex,"pastpatpoat")
# if op:
#     print("allow")
# else:
#     print("not allow")


# # ^ ---startswith ifsc code check
# regex=r"^sbin"
# op=re.match(regex,"sbin038388")
# if op:
#     print("valid ifcs code")
# else:
#     print("not valid ifsc code")


# #$---ends with and check gmail
# regex=r"com$"
# op=re.search(regex,"nani@gmail.com")
# if op:
#     print("valid gmail")
# else:
#     print("not valid gmail")



# # \d----0-9
# regex=r"\d"
# op=re.search(regex,"nani123")
# if op:
#     print("valid ")
# else:
#     print("not valid ")


regex=r"^hdfc\d+$"
op=re.search(regex,"hdfc123")
if op:
    print("valid")
else:
    print("invalid")



# # \w----(a-z,A-Z,0-9,underscore)
# regex=r"\w"
# op=re.search(regex,"hello123_4")
# if op:
#     print("valid ")
# else:
#     print("not valid ")


# \s----whitespace
# regex=r"\s"
# op=re.search(regex,"nan_ i123")
# if op:
#     print("valid ")
# else:
#     print("not valid ")


#[]----must and should contain abc in anywhere
# regex=r"[abc]"
# op=re.search(regex,"ncan_i12b3")
# if op:
#     print("valid ")
# else:
#     print("not valid ")  


# vowels must 
# regex=r"[aeiou]"
# op=re.search(regex,"nUcan_ie12b30")
# if op:
#     print("valid ")
# else:
#     print("not valid ")



#chech e-i #only check anyone
# regex=r"[e-i]"
# op=re.search(regex,"n")
# if op:
#     print("valid ")
# else:
#     print("not valid ")

# upper one also check
# regex=r"[A-Z]"
# op=re.search(regex,"aAbc")
# if op:
#     print("valid ")
# else:
#     print("not valid ")

#pure vowels not allowed
# regex=r"[^aeiou]"
# op=re.search(regex,"welcome")
# if op:
#     print("valid ")
# else:
#     print("not valid ")

#accept a input when it have legth more than 5
# regex=r"\w{5,}"
# op=re.search(regex,"welcome")
# if op:
#     print("valid ")
# else:
#     print("not valid ")


#accept a input when it have legth more than 5 and less tha 10 and end with $ must
# regex=r"^\w{5,10}$"
# op=re.search(regex,"welcomaasdff")
# if op:
#     print("valid ")
# else:
#     print("not valid ")

#pancard checking first five characters and then numbers four digits and last one must and should last one--one character
# regex=r"^[A-z]{5}+[0-9]{4}+[A-Z]{1}$"

# op=re.search(regex,"THARU1234R")
# if op:
#     print("valid")
# else:
#     print("not")

# ##input from user
# import re

# regex = r'^[A-Z]{5}[0-9]{4}[A-Z]$'


# pan = input("Enter PAN Number: ").upper()

# if re.fullmatch(regex, pan):
#     print("Valid PAN Number")
# else:
#     print("Invalid PAN Number")




