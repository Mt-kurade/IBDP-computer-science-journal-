'''
Instruction: 
Write a Python program that checks if a user is eligible to watch a movie based on age and returns a customized message.

Ask the user to input their name and age.

Use an if/else statement to check if the user is:

· Under 13 → Not allowed

· Between 13 and 17 → Parental guidance required

· 18 or older → Allowed

Create a function called check_eligibility(age) that:

· Takes age as input

· Returns the eligibility message as a string

Print a final message like:

Hello, Alice! You are 15 years old.

Result: Parental guidance required to watch the movie.
'''

name = str(input("Please enter you name:"))
age = int(input("Please enter you age:"))

def check_elifibility(age):
    if age < 13: 
        return "Sorry, you are underaged and not allowed to watch the movie"
    elif 13<= age<18:
        return "Parental guidance is required to watch this movie"
    else: 
        return "You are allowed to watch the movie"
    
message = check_elifibility(age)
print(f"Hello,{name}!, you are {age} years old. \n Result:{ message}")

