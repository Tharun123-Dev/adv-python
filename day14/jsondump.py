import json
ip=[1,2,3,4]

#converting string and insert to json file
with open("data.json","w") as f:
    a=json.dumps(ip)
    f.write(a)

#dump are used to conversion json and stores file
with open("data.json","w") as f:
    json.dump(ip,f)
      