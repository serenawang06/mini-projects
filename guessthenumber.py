import random

num = random.randrange(0, 101)
print(num)
guess = int(input("Enter a number between 0 and 100: "))

while guess != num:
    if guess > num:
        print("lower")
    elif guess < num:
        print("higher")
    elif guess == num:
        break
    else:
        print("Enter a valid guess")
    guess = int(input("Enter a number between 0 and 100: "))

print("Congrats! You guessed it!")
