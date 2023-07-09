
print("Hello world")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
#Variables and Data Types
character_name="Johnny"
character_age="60"
print("There once was a man named " +character_name+",")
print("he was " + character_age + "  years old.")
character_name="Brad"
print("He really liked the name " +character_name+",")
print("but didn't like being " +character_age+"")
#Strings
#Working w Strings
print("Tony\nSoprano")
#\n(escape character) for inserting a new line or any other symbol
print("Anthony\"/Soprano")
#string variable
show="The Sopranos"
print(show+ " is peak")
#appending one string onto another called concatenation
#function(can be used to modify or obtain information about the string)
print(show.upper().isupper())
#converted the whole thing into uppercase so got a True value back
#len(length function will tell the no of characters)
print(len(show))
print(show[7])
#[7] no inside the square bracket will print out the character which is in the sq bracket
print(show.index("Sopr"))
#index function locates a specific character inside of string
print(show.replace("Sopranos","Corleone's"))
#Numbers
#Working with Numbers
print(-7.5)
print(7*(2+4))
#parentheses can be used to specify the order of operat
print(10%3)
number=-7
print(str(number)+ " my lucky number")
#str converts the number into string
print(abs(number))
#abs is used for absolute value of the number
print(pow(7,2))
#pow is used to take number to a certain power
print(max(6,4))
#max will give the maximum val
print(min(7,2))
#min will give the min value
print(round(7.5))
#round is used to roundoff the no
#"from math import *" is used to access more math functions

