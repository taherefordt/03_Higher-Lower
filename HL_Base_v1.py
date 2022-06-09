import random
import math
from math import log2
from turtle import clear

def decorator(text, decorator, lines):

    ends = decorator * 4
    statement = "{} {} {}".format(ends, text, ends)
    text_length = len(statement)

    if lines == "3":
        print("|+=--", decorator * text_length, "--=+|" )
        print("|+=--", statement, "--=+|")
        print("|+=--", decorator * text_length, "--=+|" )

    if lines == "1":
        print("|+=--", statement, "--=+|")

def high_low_check(low_bound, high_bound, error, error_num, guesses):

    valid = False
    while not valid:

        try:

            guess = int(input("\n|+=--select a number between {} and {} --=+| \n\n".format(low_bound, high_bound)))

            if secret_num < guess < high_bound + 1:
                print("|+=-- lower --=+|")

            elif secret_num > guess > low_bound - 1:
                print("|+=-- higher --=+|")

            elif guess == secret_num:
                print("you guessed it")
                valid = True

            else:
                print(error)


        except ValueError:
            print(error_num)

def choice_check(question, valid_answer, error):

    # Loop to keep the question going till answered properly
    valid = False
    while not valid:

            response = input(question).lower()
            
            for word in valid_answer:
                if response == word[0] or response == word:
                    return word
            
            print(error)
            print()

def instructions():
    print()
    print("|+=--         How to play 'higher lower'          --=+|")
    print("|+=--                                             --=+|")
    print("|+=--   1. Choose numbers as boundaries           --=+|")
    print("|+=--      to guess between (default is 1 - 100)  --=+|")
    print("|+=--                                             --=+|")
    print("|+=--   2. choose how many rounds you want        --=+|")
    print("|+=--      to play with your selected bounds      --=+|")
    print("|+=--                                             --=+|")
    print("|+=--   3. If the secret number is more           --=+|")
    print("|+=--      than your guess Joe will say 'higher'  --=+|")
    print("|+=--      Otherwise he  will say 'lower'         --=+|")
    print("|+=--                                             --=+|")
    print()
    print("( quit anytime by guessing 1 number above the high number)")
    print()

# Yeno = yes + no
yeno_answer = ["yes", "no"]

# Other variables for later use
guesses_made = 0


# Asks user if they have played before and shows instuctions if not

intro = decorator("Welcome to Higher Lower", "=", "3")

played_before = choice_check("|+=-- Have you played before? --=+|\n\n", yeno_answer, "|+=-- Please answer yes or no --=+|")

if played_before == "no":
    instructions()

# Asks if user wants to play with custom numbers
custom_numbers = choice_check("\n|+=-- would you like to play with custom numbers? --=+|\n\n", yeno_answer, "|+=-- Please answer with yes or no --=+|")

# User chooses what the custom numbers should be
if custom_numbers == "yes":
# Loops till the user has chosen valid numbers
    lownum_chose = False
    while not lownum_chose:

        try:
            low_num = int(input("\n|+=-- lowest number? --=+|\n\n"))

            if low_num <= 0:
                    print("|+=--Choose a larger number --=+|\n")
                
            else:
                lownum_chose = True

        except ValueError:
            print("|+=-- Choose an integer (number without decimals) --=+|\n")

        # If the high number is too small it asks again
    try:

        highnum_chose = False
        while not highnum_chose:

            high_num = (int(input("\n|+=-- highest number? --=+|\n\n")) + 1)

            if high_num - 1 <= low_num:
                print("|+=--Choose a larger number --=+|")
            
            else:
                highnum_chose = True
                
        valid = True
    except ValueError:
        print("|+=-- Choose an integer (number without decimals) --=+|")

# If they dont choose it uses the default
else:
    high_num = 101
    low_num = 1


# Gives user the minimum guesses
guesses_total = math.ceil(log2(high_num - 1)) + 1


# Other variables for later
guesses_made = 0
rounds_played = 0
win_loss = ""
game_summary = []

guess = 0

# Asks user if they want to do endless mode
rounds_total = int(input("|+=-- How many rounds do you want to play? type 0 for endless --=+|"))

if rounds_total == 0:
    rounds_total = 9999999999999999


playing = True

# Loops the game until its finished
while playing:

    rounds_played += 1

    # If youve used all your rounds it will stop the game
    if rounds_played == rounds_total:
        playing = False

    # List of numbers guessed this round
    already_guessed = []


    # Randomly chooses a secret number
    secret_num = random.randint(low_num, high_num - 1)
    guesses_made = 0
    

    # Loops the game till done
    while guesses_made != guesses_total:

        try:
            # Usuer guesses a number between the bounds
            guess = int(input("\n\n|+=--     Round {}:     Guess: {} of {}          --=+|\n|+=-- Select a number between {} and {} --=+|\n".format(rounds_played, guesses_made + 1, guesses_total, low_num, high_num - 1)))
            
            # Appends the guess to a list
            already_guessed.append(guess)

            guesses_made += 1 

            # If the user chooses to exit this chunk will stop the game
            if guess == high_num:
                guesses_made = guesses_total
                playing = False

            # Determines wether or not the user guess is valid
            else:
                if secret_num < guess < high_num + 1:
                    print("|+=-- Lower --=+|")

                elif secret_num > guess > low_num - 1:
                    print("|+=-- Higher --=+|")

                elif guess == secret_num:
                    print("|+=-- You guessed it --=+|")
                    break

                else:
                    print("|+=- Choose a number between the bounds --=+|")

        except ValueError:
            print("|+=-- Please choose a positive integer --=+|")   


    print("|+=-- The secret number was {} --=+|".format(secret_num))
    
    # If the user won this chunk will make sure its correctly put in the list
    if guess == secret_num:
        win_loss = "|+=-- Win --=+|\n"

    elif guess != secret_num and guess != high_num:
        win_loss = "|+=-- Loss --=+|\n"

    # Appends the numbers guesses as well as win history
    game_summary.append(already_guessed)
    game_summary.append(win_loss)

    

history_check = choice_check("|+=-- Do you want to see game history? --=+|\n", yeno_answer, "|+=-- Please answer yes or no --=+|\n")

if history_check == "yes":
    for item in game_summary:
        print(item)