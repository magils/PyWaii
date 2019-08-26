import random

coin_sides = ('head',"tails")

guess = ""

while guess not in coin_sides:
    guess = input("Guess the coin toss! Enter heads or tails:")

toss = random.choice(coin_sides)

if toss == guess:
    print("You got it!")
else:
    guess = input("Nope! Guess again:")

    if toss == guess:
        print("Now you got it!")
    else:
        print("Sorry, but you need more luck")