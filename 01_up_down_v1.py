import random


def yes_no(question, valid_answer, error):

    # Loop to keep the question going till answered properly
    valid = False
    while not valid:

            response = input(question).lower()
            
            for word in valid_answer:
                if response == word[0] or response == word:
                    return word
            
            print(error)
            print()

def high_low_check(low_bound, high_bound):

    valid = False
    while not valid:

        guess = int(input("select a number between {} and {} ".format(low_bound, high_bound)))

        if guess == secret_num:
            print("nice")
            break
            
        elif guess < secret_num:
            print("higher")
        
        elif guess > secret_num:
            print("lower")

# Yeno = yes + no
yeno_answer = ["yes", "no"]


high_num = int(input("highest number? "))
low_num = int(input("lowest number? "))

valid = False
while not valid:
            
    for item in range (0,1):

        secret_num = random.randint(low_num, high_num)

    high_low_check(low_num, high_num)

    print(secret_num)