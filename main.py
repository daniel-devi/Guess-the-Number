import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 1
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
            attempts = attempts+1
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
            attempts = attempts+1

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!, after {attempts} Tries')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    attempts = 1
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
            attempts= attempts+1
        elif feedback == 'l':
            low = guess + 1
            attempts = attempts+1

    print(f'Yay! The computer guessed your number, {guess}, correctly!, After {attempts} Attempts')


chose = int(input("Choose 1 to guess or Choose 2 to have your number guessed\n"))

if chose == 1 :
    highest = int(input("A number Between 1 to what "))
    guess(highest)
elif chose == 2:
    highest = int(input("A number Between 1 to what "))
    computer_guess(highest)
    
else:
    print("Invalid Response")
    chose = int(input("Choose 1 to guess or Choose 2 to have your number guessed\n"))

    if chose == 1 :
        highest = int(input("A number Between 1 to what "))
        guess(highest)
    elif chose == 2:
        highest = int(input("A number Between 1 to what "))
        computer_guess(highest)
    
    else:
        print("You made the Mistake Twice You Dead Brain Re Run the Code and Choose 1 Or 2 ok")
    
