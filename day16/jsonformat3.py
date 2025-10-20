import json
ip=["apple","banana","grapes"]
#store to file
# with open ("file4.json","w") as f:
#     json.dump(ip,f)
#read firts and add existing one
# ip1="pineapple"
# with open ("file4.json","r") as f:
#     data=json.load(f)#data will change from json string to list
#     if ip1 not in data["fruits"]: 
#      data["fruits"].append(ip1)#new element will append into the list
#     else:
#        print(f"{ip1} already exist")
# # # #insert don show file to store
# with open ("file4.json","w") as f:
#     json.dump(data,f)
#     print("update successfully")

# #remove graps from the list for authorised persons
# remove_element="grapes"
# file_name="file4.json"
# user="nani"
# with open(file_name,"r") as f:
#     data=json.load(f)
#     if user in data["user"] :
#      if remove_element not in data["fruits"]:
#         print(f"{remove_element} not available")
#      else:
#         data["fruits"].remove(remove_element)
#         print("remove succesfully")
#         print("user authorised")
#     else:
#        print("u re not authorised to perform remove operations")

# # #then see
# with open (file_name,"w") as f:
#     json.dump(data,f)

# #adding operation only authorised persons
# file_name="file4.json"
# user="nani"
# adding_element=input("enter fruit: ")
# with open(file_name,"r") as f:
#     data=json.load(f)
#     if user in data["user"] :
#      if adding_element in data["fruits"]:
#         print(f"{adding_element} already exist ")
#      else:
#         data["fruits"].append(adding_element)
#         print("user authorised for adding")
#     else:
#        print("u re not authorised to perform adding operations")

# # #then see
# with open (file_name,"w") as f:
# #    json.dump(data,f)


