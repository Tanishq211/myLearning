#building a guessing game
print("Guess The Word!")
print("An automotive brand")
secret_word="Mercedes"
guess = ""
guess_count=0
guess_limit=3
out_of_guesses=False
while guess!=secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
     guess=input("Enter guess: ")
     guess_count+=1
    else:
       out_of_guesses=True
if out_of_guesses:
   print("Out of Guesses,YOU LOSE!")
else:
   print("You Win!")
#for loop
#a for loop is a special type of loop in Python which allows us to loop over different collection of items
for letter in"Android iOS":
    print(letter)
members=["Tony","Silvio","Paulie"]
for member in members:
   print(member)
for index in range(24):
    print(index)
for index in range(12,24):
   print(index)
#len function is used to figure out the no of elements
for index in range(len(members)):
   print(members[index])

