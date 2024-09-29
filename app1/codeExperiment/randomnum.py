import math 
# from random import randint
import random

print("Welcome to the game: ")

lower_bound =int( input("enter lower bound number: "))
upper_bound = int(input("enter upper bound number : "))

# Random_rnd = randint (lower_bound, upper_bound)
Random_rnd = random.randint(lower_bound,upper_bound)

print(Random_rnd)