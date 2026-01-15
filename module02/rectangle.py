
print("This program calculates the area and perimeter of a rectangle based on the width and height you provide.")

rectangleWidth = input("Enter rectangle width: ").strip()
rectangleHeight = input("Enter rectangle height: ").strip()

try:
    width = float(rectangleWidth)
    height = float(rectangleHeight)
    if width < 0 or height < 0:
        raise ValueError
except ValueError:
    print("Invalid width or height")
    exit()

rectangleArea = width * height

print("Rectangle area:", rectangleArea)
print("Rectangle perimeter:", 2 * (width + height))
