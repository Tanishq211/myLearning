#exponent function
#exponent function allows us to take a number and raise it to a specific power
def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result
print(raise_to_power(2,4 ))
#2d lists and nested loops
number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]

]
for row in number_grid:
    for col in row:
        print(col)
#building a translator
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
           if letter.isupper():
               translation=translation+"G"
           else: 
               translation=translation+"g"
        else:
            translation=translation+letter
    return translation
print(translate(input("Enter a phrase: ")))
