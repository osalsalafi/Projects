# -------------- Word Guessing Game -------------
# Guessing names, the software will choose a name
# then the user must guess this name by entering 
# letter by letter, the user will have 12 chances
import random

# Names to the list
names = ['Ahmed','Osama','Ali','Khaled','Wafaa','Abdullah','Salma','Nouf','Safwan','Adnan','Omer','Afnan']

# Welcoming sentence
your_name = input("Enter your name : ")
def hello (your_name):
    return f"Hello {your_name}, your are most welcome to Word Guessing Game"
print(hello(your_name))

random_name = random.choice(names)
print("------------------ Start the challenge -----------------")
print(f"------- The name will be under these starts {'*'*len(random_name)} ------")
turns = 12
guesses = ''
stars = 1
while turns > 0 :
    guess = input("Enter a character : ")
    guesses += guess
    if random_name.startswith(guesses):
        print(f"Good guess : {guesses}{'*'*(len(random_name)-stars)}")
        stars += 1
        if guesses == random_name :
            print("Congrats, You got the correct answer")
            break
    else :
        guesses = guesses[:-1]
        print(f"Try another character : {guesses}{'*'*(len(random_name)-stars)}, you have {turns-1} chances")
        turns -= 1 

if guesses != random_name :
    print("Unfortunately, you did not get the correct answer, try again")

