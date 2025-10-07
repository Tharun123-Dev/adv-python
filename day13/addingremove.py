import json

names=["harish","nani","tharun"]

# #save to file first
with open('product.json','w') as f:
    json.dump(names,f,indent=4) #indent===one by one space

#read list back from file
with open('product.json','r') as f:
    names_file=json.load(f)
print(names_file)

#add new names
new_names=[input("enter name: "),input("enter name: ")]
names_file.extend(new_names)
print(names_file)

#again dump to that
with open('product.json','w') as f:
    json.dump(names_file,f,indent=4)


#removing if existing if ot error shown
remove_name=input("enter a name: ")
try: 
  if remove_name in names_file:
    names_file.remove(remove_name)
    print(names_file)
except ValueError:
    print("enter correct name")

#again updated final list
with open('product.json','w') as f:
    json.dump(names_file,f,indent=4)

#read list back from file
with open('product.json','r') as f:
    names_file=json.load(f)
print(names_file)






#transforming data one place to another place 
#to add data in json dump
#to read data from json file
#earlier we have performed crud operations on text data so np need to json there
#now i want to perform crud operations on data structures like list tuple dict
#we cant direct perform on them using files.so we need to store data in json format
#for east communication and for easy manipulation


# import json
# data={'name':'json','age':24,"gender":"male"}
    #use inserting for dump method--import json
# op=json.dumps(data)
# print(type(op)) #string provide
# print(data["name"]) 


#it is applicable for only string  
#will perform json methods only on objects/dictionaries

#load===convert to json object to original form

# op2=json.loads(op)
# print(type(op2))



#example for file

# import json

# list=['harish','kiran','vikas']
# with open('products.json','w') as f:
#     # data_json=json.dumps(list)
#     data_json=str(list)
#     f.write(data_json)

# with open('products.json','r') as f:
#     res=f.read()
#     print(res) #its showned lis but in string

# with open('products.json','r') as f:
#     res=f.read()
#     cnvrt_data=json.load(res)
#     print(cnvrt_data[1]) #its showned lis but in string


#add few names into existing list in the file
# new_names=["nani","tharun"]
# with open('products.py','w') as f:
#     ins=json.dumps(list)
    
#     f.write(ins)

#remove any name

# with open('products.py','r') as f:
#     ins=json.loads(f)
    
#     f.read(ins)




