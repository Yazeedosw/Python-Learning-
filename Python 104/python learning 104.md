# Scope
---------------------------------------------------------------------------------------

## Local Scope : 
---------------------------------------------------------------------------------------

- is local for example if variable inside a function i can not print it from outside (see example below)
```
def func():
    name = "Ahamd"
    print(name)
# Here i can call the func and will print "Ahmad"
func()
print(name)
# Compare to this I can not print(name) because the variable inside the function"


#convert the Local to global using global function:

def func():
    global name
    name = "Ahamd"
    print(name)

func()
print(name)

# in convert example i use "global name " so that i can use print. 
```
---------------------------------------------------------------------------------------

## Global Scope : 
---------------------------------------------------------------------------------------

- we can reach to variable from anyehere in the code
```
name = "Mohammed"

def func():
    print(name)

func() #here i can call the the function that will print the name
print(name) #Also, I can called due to variable outside the function
```
---------------------------------------------------------------------------------------

# Module
---------------------------------------------------------------------------------------

Module: allow us to divide our work to section, the Module end with extension .py

## import
- use to import Module from .py and you can call the function

## import and from
- if the module have a high number of function and you only need one use import and from Ex:
```
from (name of module) import (function name)
```
## as : to alter the name of module
```
import module as (alter name )
```
---------------------------------------------------------------------------------------

# Files
---------------------------------------------------------------------------------------

## open ("file name ", "Mode")

| Mode | Description                                                                                                                      |
|------|----------------------------------------------------------------------------------------------------------------------------------|
| **r**    | Opens the file in read mode.                                                                                                 |
| **w**    | Opens the file in write mode, deleting the contents if the file already exists.                                              |
| **x**    | Opens the file in create mode, failing if the file already exists.                                                           |
| **a**    | Opens the file in append mode, adding text below the existing text if it exists, or creating a new file if it doesn't exist. |


---------------------------------------------------------------------------------------
# Exception Handling
---------------------------------------------------------------------------------------

## except & try
```
try:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    print("the result = ", num1 / num2)

except:
    print("Error!!")

print("End of program")
```
## else
```
try:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    print("the result = ", num1 / num2)

except:
    print("Error!!")

else:
    print("No error")
```
## finally
```
try:
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    print("the result = ", num1 / num2)

except:
    print("Error!!")

else:
    print("No error")

finally:
    print("end of the program ")
```

## Use except to specify the type of error
```
myList = [1,2,0]
try:
    print("the result = ", myList[4] / myList[2])
except ZeroDivisionError:
    print("ZeroDivisionError!!")

except IndexError:
    print("IndexError!!")

## assert
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0

except :
    print("Not an even number!")
else:
    evenNumber = num / 2
    print (evenNumber)
```
## raise
```
age = int(input("Enter your age:"))
if age < 18:
    raise Exception ("Sorry, This game for more than 18 age")

print("Start game")
```
---------------------------------------------------------------------------------------



