
print("This program will ask for three integers and then compute their sum, product, and average.")

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

num1 = get_integer("Enter the first integer: ")
num2 = get_integer("Enter the second integer: ")
num3 = get_integer("Enter the third integer: ")

total_sum = num1 + num2 + num3
product = num1 * num2 * num3
average = total_sum / 3

print("Sum of the three integers:", total_sum)
print("Product of the three integers:", product)
print("Average of the three integers:", average)