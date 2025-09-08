#shallow copy
import copy  

info = {"details": {"name": "nani", "city": "hyd"}}  

x = copy.copy(info)  
y = copy.copy(info)  
x['details']["city"]="wgl"
print(info)
print(x)
print(y)



#deep copy

info = {"details": {"name": "nani", "city": "hyd"}}  

x = copy.deepcopy(info)  
y = copy.deepcopy(info)  
x['details']["city"]="wgl"
print(info)
print(x)
print(y)


#example 2
#shallow copy 

score_board={"score":{"runs":135,"wickets":4}}
nani=copy.copy(score_board)
tharun=copy.copy(score_board)
nani["score"]["wickets"]="6"
print(score_board)
print(nani)
print(tharun)

#deep copy

score_board={"score":{"runs":135,"wickets":4}}
nani=copy.copy(score_board)
tharun=copy.copy(score_board)
nani["score"]["wickets"]="6"
print(score_board)
print(nani)
print(tharun)