print("This program calculates the area of a circle for a valid radius you provide.")
circleRadius = input("Enter circle radius: ").strip()

try:
    radius = float(circleRadius)
    if radius < 0:
        raise ValueError
except ValueError:
    print("Invalid radius")
    exit()

circleArea = 3.14159 * radius * radius

print("Circle area:", circleArea)
