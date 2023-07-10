#functions
#function is a collection of code which is used to perform specific tasks
#it is used when we have a group of code which is used to perform a specific task only
#def is a keyword to use when we want to use a function
#for the code to be considered the code needs to be under the same indentation level as the function anything outside of it is not considered
def say_hi(name, age):
    print("Hello "+name+", you are"+age)
#the function does not print without a caller so we need to call the function
say_hi("Tony"," 70" )#caller
say_hi("Paulie"," 45")#caller

#return statement
#return statement is used to get information back from the function to t
def cube(num):
    return num*num*num  
print(cube(2))       
result=cube(2)
print(result)

#if statements
is_male=True
is_tall= True
if is_tall and is_male:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and (is_tall):
    print("you are not a male but are tall ")   
else:
    print("Neither you are tall nor a male")
#if statements and comparisons
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(3,74,5))
#'>=' are called comparsion operators