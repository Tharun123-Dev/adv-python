#1 syntax error 
#if True
print(10)

#fixed this with exception handling
if True:
    print("nani")

#2 zero division error
a=int(input("enter a number: "))
x=a/0

#fixed with exception handling
a=int(input("enter a number: "))
try:

    x=a/0
except ZeroDivisionError:
    print("not divisible")
#fixed one
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Division by zero not allowed")

#3.ValueError
#Ask the user for their age. Handle the case when the user enters a string instead of a number.

#value error ex:int("abc")
a=int(input("enter a number: "))
print(a)

# #fixed
try:
    a=int(input("enter a number"))
except ValueError:
    print("this is value error")
except:
    print("something")


#fixed one
try:
    x = int("abc")
except ValueError:
    print("Invalid number")

# 4.TypeError
# Try adding an integer and a string together. Handle the error.
a="nani"
b=5
print(a+b)
#fixed
try:
    a="nani"
    b=5
    c=a+b
except TypeError:
    print("type error")
except:
    print("something wrong")


#5.Finally Block
#Write a program that takes an integer input. No matter what error occurs, print "Program Completed" using finally.
#zero devision error
a=5
b=0
print(a/b)

#fixed with finally block
try:
    a=5
    b=0
    print(a/b)
except ZeroDivisionError:
    print("undefined")
finally:
    print("fixed")

#process 3
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except Exception as e:
    print("Error:", e)
finally:
    print("Program Completed")


# 6.Multiple Exceptions
# Ask the user for two numbers and perform division. Handle both ZeroDivisionError and ValueError separately.
try:
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    print(a/b)
except ZeroDivisionError:
    print("this is not devisible by zero")
except ValueError:
    print("does not take string instead of int")
except:
    print('something wrong')


#7.File Handling Error
#Try to open a file named student_data.txt. If it doesn’t exist, show a proper error message.
x=open("sample.txt",'r')
data=x.read()

print(data)


x=open("exceptionhandlin.py","r")
print(x)

#fixed
try:
    x=open("exceptionhandlin.py","r")
    print(x)
except FileNotFoundError:
    print(" file doesn't exist")
except:
    print("something is wrong")

 #8.Catch All Exceptions
 #Write a program that asks for a number and prints its square. Use Exception to handle any unexpected errors.

try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except Exception as e:
    print("Unexpected Error:", e)

try:
    a=5
    b=0
    print(a/b)
except Exception as error:
    print("unexcepted error: ",error)

# 9.Custom Error Message
# If the user enters a negative age, raise a ValueError with a custom message: "Age cannot be negative!".

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Your age is:", age)
except ValueError as e:
    print("Error:", e)



#10.Safe Calculator
#Create a simple calculator (add, subtract, multiply, divide) that takes input from the user. Handle errors like invalid input, division by zero, etc.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        print("Result:", num1 / num2)
    else:
        print("Invalid operation!")
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print("Unexpected Error:", e)














