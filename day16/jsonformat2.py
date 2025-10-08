import json
ip=["apple","banana","grapes"]
#store to file
# with open ("file3.json","w") as f:
#     json.dump(ip,f)
#read firts and add existing one
# ip1="pineapple"
# with open ("file3.json","r") as f:
#     data=json.load(f)#data will change from json string to list
#     if ip1 not in data["fruits"]: 
#      data["fruits"].append(ip1)#new element will append into the list
#     else:
#        print(f"{ip1} already exist")
# # #insert don show file to store
# with open ("file3.json","w") as f:
#     json.dump(data,f)
#     print("update successfully")

# #remove graps from the lis
# remove_element="grapes"
# file_name="file3.json"
# with open(file_name,"r") as f:
#     data=json.load(f)
#     if remove_element not in data["fruits"]:
#         print(f"{remove_element} not available")
#     else:
#         data["fruits"].remove(remove_element)
#         print("remove succesfully")

# #then see
# with open (file_name,"w") as f:
#     json.dump(data,f)
