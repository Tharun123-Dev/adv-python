#decorator-- it is a function that enhance other function without modifiding the original code
# #Example
# def sum(a,b):
#     print(a+b)
# sum(1,2)
# sum("sum",5)

# #decorators

# def check_int(func):#this is the decorator name
#     def wrapper(): #wrapper use inside the function #for adding functionalities for the original functions
#         print("before original function")
#         func()
#         print("after the original function")
#     return wrapper

# @check_int   #@followed by decorator name
# def say_hello():
#     print("hello world")
# say_hello()

# #check int also
# @check_int
# def good_evng():
#     print("good evening")
# good_evng()







# #integer check
# def check_intt(fun):
#     def wrapper(a,b):
#         if type(a)!=int or type(b)!=int:
#             return "invalid inputs"
#         fun(a,b)
#     return wrapper

# @check_intt
# def sum(a,b):
#     print(a+b)
# print(sum(1,2))



# #integer check
# def check_intt(fun):
#     def wrapper(a,b):
#         if not isinstance(a,int) and not isinstance(b,int):
#             return "invalid inputs"
#         fun(a,b)
#     return wrapper

# @check_intt
# def sum(a,b):
#     print(a+b)
# print(sum(1,2))



# @check_intt
# def add_num(m, n):
#     return m + n


# print(add_num(10, 20))



# #checking string 

# def check_str(fun):
#     def wrapper(n):
#         if not isinstance(n,str):
#             return "not a name"
#         res=fun(n)
#         return res
#     return wrapper


# @check_str
# def wish(name):
#     return "hello"+name

# print(wish("123"))




# # *args,**kwrgs---all parameters are accepted in this keywords use

# def has_zero(org):
#     def wrapper(*args):
#         if 0 in args:
#             return "invalid parameters"
#         res=org(*args)
#         return res
#     return wrapper 
# @has_zero
# def params(*a):
#     print(a)
#     return "hello"
# print(params(1,2,3,2,3,4,0))



# # *args,**kwrgs---all parameters are accepted in this keywords use

# def has_zero(org):
#     def wrapper(*args):
#         if 0 in args:
#             res=org("mani")
#             return res
#         else:
            
#          res=org(*args)
#          return res
#     return wrapper 

# @has_zero
# def params(*a):
#     print(a)
#     return "hello"
# print(params(1,2,3,2,3,4,))



#parameter passed
def check_name(func):
   def wrapper(*args):
      
        names_list = list(args)
        
      
        if "babar" in names_list:
            names_list.remove("babar")
            print("Removed invalid name because he is not indian cricket player: babar")
            return names_list
        
        else:
         res=func(*args)
         return f"all are indian cricket players: {res}"
   return wrapper

@check_name
def names(*a):
   return a
print(names(input("enter a name of indian cricket player : "),
            input("enter a name of indian cricket player: "),
            input("enter a name of indian cricket player: "),
            input("enter a name of indian cricket player: ")))