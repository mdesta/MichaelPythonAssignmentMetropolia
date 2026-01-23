# Program to find the smallest and largest numbers from list of user input

# Init list to store numbers
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    # Stop if input is empty
    if user_input == "":
        break
    
    try:
        # Convert input to float and add to the list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if any numbers were entered
if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"\nSmallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("\nNo numbers were entered.")
