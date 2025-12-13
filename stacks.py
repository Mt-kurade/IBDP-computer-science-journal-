# Code 1 : Brackets are balanced using stack

brackets = input("Enter a string containing only { and }: ")

stack = []

for ch in brackets:
    if ch == '{':
        stack.append(ch)
    elif ch == '}':
        if stack:
            stack.pop()
        else:
            # More closing brackets than opening ones
            print("The string is NOT balanced.")
            break
else:

    if not stack:
        print("The string is BALANCED.")
    else:
        print("The string is NOT balanced.")


#Code 2 : Reverse order of words using stack

sentence = input("Enter a sentence: ")

words = sentence.split()
stack = []

for word in words:
    stack.append(word)

reversed_sentence = []
while stack:
    reversed_sentence.append(stack.pop())

print("Reversed sentence:", " ".join(reversed_sentence))