# Const
# Conversion factor
INCH_TO_CM = 2.54

while True:
    try:
        inches = float(input("Enter length in inches (negative value to quit): "))
        
        if inches < 0:
            print("Program ended.")
            break
        
        centimeters = inches * INCH_TO_CM
        print(f"{inches} inches = {centimeters:.2f} cm\n")
        
    except ValueError:
        print("Invalid input. Please enter a number.\n")
