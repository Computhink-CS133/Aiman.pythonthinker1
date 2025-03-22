# print("Hello from lesson 9")

import random as rand

num=str(rand.randint(1,10))
guess=input("Pick a random number between 1 to 10 ")

print("Your guess: "+ guess)
print("The number: "+ num)

print(guess==num)