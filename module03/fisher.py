# Const
SIZE_LIMIT = 42

# Wont validate input for simplicity
length = float(input("Enter the length of the zander in centimeters: "))

# Check
if length < SIZE_LIMIT:
    difference = SIZE_LIMIT - length
    print("This is baby Zander, please put it back to the lake.")
    print(f"It was {difference:.1f} centimeters below the minimum limit, which is {SIZE_LIMIT} centimeters.")
else:
    print("The zander meets the size limit. You may keep the fish.")
