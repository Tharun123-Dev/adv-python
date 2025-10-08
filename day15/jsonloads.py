import json
ip=["apple","nani","grapes"]

#first we want insert
with open("dataa.json","w") as f:
    f.write(json.dumps(ip))

#we prints without loads total string is there like print 2 that is a 
with open ("dataa.json","r") as f:
    data=f.read()
    print(data[2])

#so using loads print 2 as a nani because it taken json format
with open("dataa.json","r") as f:
    data=f.read()
    convert=json.loads(data)
    print(convert[2])

#load used for direct format like
with open("dataa.json","r") as f:
    data=json.load(f)
    print(data[2])