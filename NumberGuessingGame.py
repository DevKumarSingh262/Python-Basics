import random
# ----------------------------------------------------------------------------------------------

top_of_range = input("Enter top range: ")

if top_of_range.isdigit() or top_of_range[1:].isdigit() and top_of_range[0]=="-":
    top_of_range = int(top_of_range)
else:
    print("Please type a number next time!")
    quit()
# ----------------------------------------------------------------------------------------------

bottom_of_range = input("Enter bottom range: ")

if bottom_of_range.isdigit() or bottom_of_range[1:].isdigit() and bottom_of_range[0]=="-":
    bottom_of_range = int(bottom_of_range)
else:
    print("Please type a number next time!")
    quit()
# ----------------------------------------------------------------------------------------------
    
if top_of_range < bottom_of_range:
    print("Please use correct format(Top range is always greater than Bottom range!)")
    quit()
# ----------------------------------------------------------------------------------------------

random_number=random.randint(bottom_of_range,top_of_range)
guesses = 0
# ----------------------------------------------------------------------------------------------

while True:
    guesses += 1
    user_guess = input("Guess the Random number: ")
    if user_guess.isdigit() or user_guess[1:].isdigit() and user_guess[0]=="-":
        user_guess = int(user_guess)

        if user_guess > top_of_range or user_guess < bottom_of_range:
            print("Please type a number within range (",bottom_of_range,",",top_of_range,")")
            continue
    else:
        print("Please type a number next time!")
        continue

    if user_guess == random_number:
        print("You Got it!")
        print("Random number is:",random_number)
        break
    else:
        if user_guess > random_number:
            print("You Got it Wrong!,you were above the number ")
        else:
            print("You Got it Wrong!,you were below the number")

print("you got it in",guesses,"guessses")
    


