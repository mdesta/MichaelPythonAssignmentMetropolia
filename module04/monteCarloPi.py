import random

print("This program estimates the value of π using the Monte Carlo method.")
print("You will be prompted to enter the number of random points to generate.")
print("The larger the number of points, the more accurate the approximation will be.\n")

while True:
    try:
        N = int(input("Enter the number of random points to generate: "))
        if N <= 0:
            print("Please enter a valid positive integer Number.")
        else:
            break
    except ValueError:
        print("Please enter a valid positive integer Number.")

# Initialize counter for points inside the circle
NumberOfPointInsideCircle = 0

# Generate N random points
# Loop N times
# In every loop, generate a randome point (x,y)
# Check if the point is inside the unit circle
# If yes, increment NumberOfPointInsideCircle counter
for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 <= 1:
        NumberOfPointInsideCircle += 1

# Approximate pi
approxPi = 4 * NumberOfPointInsideCircle / N

# Print the result
print(f"\nApproximation of π using {N} random points: {approxPi}")