#getting input from users
name = input("Enter your name: ")
print("Hello "+ name + "!")
age=input("Enter your age: ")
print(name+ " You are "+age)


#building a basic calculator
num1=input("Enter a number: ")
num2=input("Enter another number: ")
result=num1+num2
print(result)


#mad libs game
color=input("Enter your color: ")
plural_noun=input("Enter your plural noun: ")
celebrity=input("Enter your celebrity: ")
print("roses are "+ color)
print(plural_noun+ " are blue")
print("i love "+ celebrity)


#working with lists
member=["Tony","Paulie","Christopher","Silvio","Vito"]
print(member[1:4])
#colon can be used to print out more than one elements 
#used for organizing and storing a bunch of different values
imp_dates=[2,15,16,1,26]
member=["Tony","Tony","Paulie","Christopher","Silvio","Vito"]
print(imp_dates)
#extend functions allows you to take list and append another list onto the end of it
#member.extend(imp_dates)
#append is used to add another element with the existing ones
#member.append("Richie")
#insert function is used to add the element at a specific index
#member.insert(4, "Richie")
#remove function to remove any element
#member.remove("Silvio")
#clear function to empty the list
#member.clear()
#pop function removes the last element which was present in the list
#member.pop()
#count function tells us how many times the element has been repeated in the list
#sort function will arrange the elements alphabetically or in ascending order
member.sort()
imp_dates.sort()
#reverse function reverses the order of elements
member.reverse()
#copy function
member2= member.copy()
print(member2)


#tuples
#tuples is a container like a list which is immutable i.e it can't be changed or modified unlike lists
variables=("x","y")
variables[1]=10
#TypeError: 'tuple' object does not support item assignment   
print (variables[1])
