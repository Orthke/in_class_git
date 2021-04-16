import random

userInput = int(input("Enter a password length: "))

pwd = ""

for i in range(userInput):
    pwd += str(chr(random.randint(97,122)))

print(pwd)