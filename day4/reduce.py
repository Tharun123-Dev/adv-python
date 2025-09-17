from functools import reduce
li=[2,4,5,7,4,5,1]
op=reduce(lambda x,y:x if x<y else y ,li)
print(op)
#example 2

li=[2,4,5,7,4,5,1]
op=reduce(lambda x,y:x+y,li)
print(op)

# example 3
li=[2,4,5,7,4,5,1]
op=reduce(lambda x,y:x+y,li,6)
print(op)

#example 4
li=[2,4,5,7,4,5,1]
op=reduce(lambda x,y:x if x>y else y ,li)
print(op)

#example smallest length
li=["i",'love','my','india']
op=reduce(lambda x,y:x if len(x)<len(y) else y,li)
print(op)
op=reduce(lambda x,y:x if len(x)>len(y) else y,li)
print(op)

op=reduce(lambda x,y:x+y,li)
print(op)


#string to number
ip1=[4,6,3,2,1]
op=reduce(lambda x,y:x*10+y,ip1)
print(op)


