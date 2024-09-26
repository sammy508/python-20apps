# mood = input('how was your mood today? \n')
# date = input("Enter today's date: \n")
# thoughts = input("enter your thoughts : \n")

# with open(f"journal/{date}.txt", 'w') as file:
#     file.write(mood)
#     file.write(thoughts)
# print(file)


# here code below is well formatted version of this code
import os

# Getting inputs
mood = input('How was your mood today?\n')
date = input("Enter today's date (format: YYYY-MM-DD):\n")
thoughts = input("Enter your thoughts:\n")

# Ensure the journal directory exists
if not os.path.exists('journal'):
    os.makedirs('journal')

# Writing to the file
file_path = f'journal/{date}.txt'
with open(file_path, 'w') as file:
    file.write(f"Mood: {mood}\n")
    file.write(f"Thoughts: {thoughts}\n")

print(f"Your entry has been saved to {file_path}.")
