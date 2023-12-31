import random

# List of 35 possible passwords
passwords = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house',
             'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound',
             'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water',
             'where', 'which', 'world', 'would', 'write']


repeat = "yes"


# Counting the number of matching letters
def matching_letters():
    common_letters = set(random_password).intersection(guess)
    print(f"{len(common_letters)} letters correct.")


# Play the game
print("Welcome to the password breaker game!\n")
while repeat.lower() == "yes":
    # Choose the game mode
    game_mode = input("Which mode would you like to play on (easy/hard)? ").lower()
    random_password = random.choice(passwords)
    # Easy mode
    if game_mode.lower() == "easy":
        attempt = 1
        while True:
            # User input a guess password
            guess = input("Enter a guess: ").lower()

            # If user type quit the game is over
            if guess == "quit":
                print(f"The password was {random_password}\n")
                break

            matching_letters()

            # user type correct password
            if guess == random_password:
                print(f"Correct! {attempt} guesses used.")
                break

            attempt += 1

        # Ask user to play again
        play_again = input("Play again (yes/no)? ").lower()
        if play_again.lower() != "yes":
            break

    # Hard mode
    elif game_mode.lower() == "hard":
        for i in range(1, 6):
            # User input a guess password
            guess = input("Enter a guess: ").lower()

            # If user type quit the game is over
            if guess == "quit":
                print(f"The password was {random_password}\n")
                break

            matching_letters()

            # user type correct password
            if guess == random_password:
                print(f"Correct! {i} guesses used.")
                break

        # Ask user to play again
        print(f"The password was {random_password}\n")
        play_again = input("Play again (yes/no)? ").lower()
        if play_again.lower() != "yes":
            break

    # let a user know the typo
    else:
        print("Please type 'hard/easy'.")

print("Thanks for playing Password Breaker Game!")
