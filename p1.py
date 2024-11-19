#this is program to guess the the number game
import random
print("hi welcome to game to guess ,this is number guessing game where u got 3 chances to guess the number .lets start game") 
guess_number = random.randrange(100)
chance = 3
guess_counter = 0
while guess_counter < chance:
    guess_counter += 1
    my_guess = int(input("enter ur guess :"))
    if my_guess == guess_number:
        print("congrats u won",guess_number ,"and you founded it right!!")
    else:
        print("ohh u lost!!",guess_number,"is the number u should have guessed!!")
    if chance >3:
        print("u have only 3 chances!! try again next time")

