import random

secret_number = random.randint(1,30)
guess = eval(input("Enter your guess: "))

if guess > secret_number :
    print("Too high!")
elif guess < secret_number :
    print("too Low!")
else:
    print("Correct!")
print("The secret number is: ", secret_number)