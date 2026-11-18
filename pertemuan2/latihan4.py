import random


choose_level = int(input("Choose level (1-3): "))
if choose_level == 1:
    max_number = 10
elif choose_level == 2:
    max_number = 30
else:
    max_number = 50
secret_number = random.randint(1, max_number)
guess = int(input(f"Enter your guess (1-{max_number}): "))

while guess != secret_number:
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    guess = int(input(f"Enter your guess (1-{max_number}): "))

    print("Correct!")
  