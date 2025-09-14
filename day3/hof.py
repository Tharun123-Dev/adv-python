# #1 add country code to phone number
# op=map(lambda x:"+91"+x,["9949693030","6309383826","9876543210"])
# print(list(op))

# #2 convert prices from dollers to rupees
# result=map(lambda x: x*83,[10,20,30,40])
# print(list(result))

# #3 filter gmail ids
# result=filter(lambda x: x.endswith("gmail.com"),["anjali@gmail.com","abc@yahoo.com","naveen@gmail.com"])
# print(list(result))

# #4 get short product names
# re=filter(lambda x:len(x)<=5,["pen","mpoiedj","notebook","tharun"])
# print(list(re))

# #5 convert names to usernames
# name=map(lambda x: x.lower()+"@gmail.com",["nani","harish"])
# print(list(name))

# #6 filter expired products
# year=filter(lambda x: x>=2025,[2025,2022,2021,2026])
# print(list(year))

# #7make credit card numbers
# credit=map(lambda x: "*"*(len(x)-4)+x[-4:] ,["123456754434568767","145282728789898976"])
# print(list(credit))

# #8 filter high salary employees
# sal=filter(lambda x : x>=40000,[25000,45000,60000,80000])
# print(list(sal))

# #9 format product lables
# fruits=map(lambda x: f"product: {x}",["mango","apple"])
# print(list(fruits))

# #10 student passed
# student=filter(lambda x: x>=40,[30,40,70,60,40])
# print(list(student))

# #11 Filter strong passwords
# strong=filter(lambda x: (len(x)>=8) and ("@" in x or "$" in x),["abc123","Admin@123","p@ssword$"])
# print(list(strong))

# #12 process transaction records
# trans=map(lambda x: int(x.split("-")[0]) ,["1000-CREDIT","500-DEBIT","1200-CREDIT"])
# print(list(trans))
# #filter credits
# credits=list(filter(lambda x: "CREDIT" in x,["1000-DEBIT","900-CREDIT"]))
# print(credits)
# #filter debits
# debits=list(filter(lambda x: "DEBIT" in x,["1000-DEBIT","900-CREDIT"]))
# print(debits)