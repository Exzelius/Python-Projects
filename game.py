from random import *

def game():
    num = randint(1,100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int (input("Enter a number between 1 and 100: "))
            attempts+=1
            if(guess < num):
                print("Your guess is too low!\n")
            elif(guess > num):
                print("Your guess is too high!\n")
            else:
                print(f"You guessed the number {guess} in {attempts} attempts!\n")
                guessed=True
        except ValueError:
            print("Please Enter a Valid Number!\n")

if __name__== "__main__":
    game()
