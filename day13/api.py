import requests
import json
#api also have similar names like---url endpoint 
# api="https://jsonplaceholder"


api="https://fakestoreapi.com/products"

# #crud -->get post put?patch delete
# data=requests.get(api)
# print(data.json())

#post we can use
movies={
    "bahubali": "600",

}
#updation
movies["bahubali"]="700"

j_son=json.dumps(movies)
print(j_son)
#type check
print(type(j_son))

# #object wise to convert
# j_son=j_son.json()
# print(type(j_son))

#again string-orinal methods like dictionary
j_son=json.loads(j_son)
print(type(j_son))
