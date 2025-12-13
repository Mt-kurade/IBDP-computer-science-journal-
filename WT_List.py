#Method: Using for statement to collect marks and print report
Roll_number = input("Please enter your roll number: ")
Name = input("Please enter your name: ")
Class = input("Please enter your class: ")

Marks = []
for i in range(1, 6):
    mark = float(input(f"Please enter the marks for subject {i}: "))
    Marks.append(mark)

average = sum(Marks) / 5

if average >= 85:
    result = "Distinction"
elif average >= 75:
    result = "Merit"
elif average >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\n--- Student Report ---")
print(f"1. Name: {Name}")
print(f"2. Roll Number: {Roll_number}")
print(f"3. Class: {Class}")
print("4. Marks:")
for idx, mark in enumerate(Marks, 1): 
    print(f"   Subject {idx}: {mark}")
print(f"5. Average Marks: {average:.2f}") #.2f prints to 2 decimal places 
print(f"6. Result: {result}")

'''
Psuedocode logic breakdown:
--Start--
1. Prompt user for roll number and store in Roll_number
2. Prompt user for name and store in Name
3. Prompt user for class and store in Class 

4. Create empty list Marks 

5. FOR subject number form 1 to 5 DO
    a. Prompt user for marks and current subject 
    b. convert input to ofloat and add to marks list 

6. Calculate average as sum or marks diveded by 5 (for 5 subjects )

7. IF averae >= 85 then
    result = "Distinction"
ELSE IF average >= 75 THEN 
    result = "Merit"
ELSE IF average >= 40 THEN
    result = "Pass"
ELSE
    result = "Fail"

8.PRINT stuent report: 
    a. Name
    b. Roll number 
    c. Class 
    d. Marks for each subject 
    e. Average marks (to 2 decimal places)
    f. Final result 

'''


#Method 2: Using indiviual print statements to create list 

mark1 = float(input("Please enter the marks for subject 1: ")) #Float to take into considereation decimal marks 
mark2 = float(input("Please enter the marks for subject 2: "))
mark3 = float(input("Please enter the marks for subject 3: "))
mark4 = float(input("Please enter the marks for subject 4: "))
mark5 = float(input("Please enter the marks for subject 5: "))

Marks = [mark1, mark2, mark3, mark4, mark5] #List of marks 
Marks_average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5 #Average calculation

if Marks_average >= 85:
    result = "Distinction"
elif Marks_average >= 75:
    result = "Merit"
elif Marks_average >= 40: 
    result = "Pass"
else: 
    result = "Fail"

print("\n--- Student Report ---") #\n  is an escape character that stands for new line, it creates a new line before it prints (---student report---)
print(f"1. Name: {Name}")  #f stands for f-string (formatted string litreal and allows you to insert variable directly inside curly braces {} within the string) Without an f since the variable name is printed literally and not its value. 
print(f"2. Roll Number: {Roll_number}")
print(f"3. Class: {Class}")
print("4. Marks:")
print(f"   Subject 1: {mark1}")
print(f"   Subject 2: {mark2}")
print(f"   Subject 3: {mark3}")
print(f"   Subject 4: {mark4}")
print(f"   Subject 5: {mark5}")
print(f"5. Average Marks: {Marks_average:.2f}") #.2f prints to 2 decimal places
print(f"6. Result: {result}")
