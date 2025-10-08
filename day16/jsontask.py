import json
ip=["apple","banana","grapes"]
#store to file
with open ("file.json","w") as f:
    json.dump(ip,f)
#read firts and add existing one
ip1="pineapple"
with open ("file.json","r") as f:
    data=json.load(f)#data will change from json string to list
    data.append(ip1)#new element will append into the list
#insert don show file to store
with open ("file.json","w") as f:
    json.dump(data,f)
    print("update successfully")