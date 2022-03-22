# Step 1
# we need to limit the number of times that the user is going to make guesses
# Step 2
# Create a range of numbers so that the user gets to guess a number within the range.
# Range can be from 1-10 so this means the user will choose a number between 1-10
# Step 3
# set ranges to decide if the guesses are either too large or too small
# Step 4
# Ask the user to input their name so we can welcome the user
# Step 5
# We use a while loop to permit repetitive guessing
# step 6
# If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
# Step 7
# Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
# Step 8
# And if the user guessed in a minimum number of guesses, the user gets a “Wow!] you guessed right! ” as an Output.
# Step 9
# Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.

        #ALGORITHM

import random                #this module is used to pick a random number in a given range
guessesTaken = 0
number = random.randint(1, 50)   #we are guessing a random integer between 1 and 50
print('Welcome to the guessing game!\n Guess a number between 1 and 50.')
while guessesTaken < 6:           #the player should be able to guess the number in less than 6 trials
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    guessesTaken += 1

    if guess < number:
        print('Try again! Your guess is too low.')

    if guess > number:
        print('Try again! Your guess is too high.')

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')
        break     #stops the program when the player gets the answer right

if guess != number:
    number = str(number)
    print('\nSorry, the number I was thinking of was ' + number)  #tells the player the random number