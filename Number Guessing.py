import random

# Taking Inputs
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

# Generating random number between the lower and upper bounds
x = random.randint(lower, upper)

# Determining the number of chances based on the difference between upper and lower bounds
if upper - lower <= 10:
    max_chances = 3
else:
    max_chances = 5

print(f"\nYou've only {max_chances} chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of guesses depends upon range
while count < max_chances:
    count += 1
    # Taking guessing number as input
    guess = int(input("Guess a number: "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in", count, "try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses, shows this output.
if count == max_chances and x != guess:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
