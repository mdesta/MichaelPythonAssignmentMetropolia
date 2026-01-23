import random

# Computer selects a random number between 1 and 10
secret_number = random.randint(1, 10)


while True:
    try:
        guess = int(input("Please enter a valid integer number between 1 and 10. You can also pick 1 or 10.\n"))
        
        if guess < 1 or guess > 10:
            print("Please enter a valid integer number between 1 and 10. You can also pick 1 or 10.\n")
            continue
        
        # Exit game if "" or Enter is pressed
        if guess == "":
            print("Game exited.")
            break

        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print("Correct")
            break  # Exit the loop when guessed correctly
            
    except ValueError:
        print("Invalid input. Please enter a valid integer number between 1 and 10. You can also pick 1 or 10.")
