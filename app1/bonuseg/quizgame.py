import json

with open("journal/quizgame.json",'r') as file:
    content = file.read()

data = json.loads(content)  # converts data into list

for question in data:  # here question is a current dictionary
    print(question["question"])                                 #enumerate(...) goes through each item in that list and 
    for index, alternative in enumerate(question["alternative"]):   #returns a tuple containing the index (starting from 0) and the value (the alternative)
        print(index+1,":", alternative)
    user_choice = int (input("ENter your answer: "))
    question["user_choice"] = user_choice

score = 0

for index, question in enumerate(data):
    if question['user_choice'] == question['correct']:
        score = score+1
        result = "correct answer"
    else:
        result= "Worng answer"    
    message= f"{index+1} {result}: Your answer is {question['user_choice']}, " \
             f"correct answer :{question['correct']}"
    
    print(message)
    print(f"Your total score is: {score}")