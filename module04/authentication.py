username = "python"
password = "rules"

MAX_ATTEMPTS = 5
attempts = 0

while attempts < MAX_ATTEMPTS:
    # Lets strip any extra whitespace from input a bit extra spiciness :D
    username_input = input("Enter username: ").strip()
    password_input = input("Enter password: ").strip()
    
    if username_input == username and password_input == password:
        print("Welcome!")
        break
    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts
        if remaining == 1:
            print(f"Incorrect credentials. This is your last attempt.\n")
        elif remaining > 1:
            print(f"Incorrect credentials. You have {remaining} attempts remaining.\n")
else:
    print("Access denied.")
