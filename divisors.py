userInput = int(input("Enter a number to see its divisors: "))


divisors = []

for i in range(userInput, 1, -1):
    if userInput % i == 0:
        divisors.append(i)


print(divisors)
