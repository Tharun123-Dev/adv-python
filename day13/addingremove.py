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



