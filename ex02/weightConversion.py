
print("This program converts weights from ancient units (talents, pounds, lots) to modern units (kilograms and grams).")

# Consts
LOTS_PER_POUND = 32
POUNDS_PER_TALENT = 20
GRAMS_PER_LOT = 13.3

# Input
talents = float(input("Enter talents:\n"))
pounds = float(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))

# Total in lots
total_lots = (
    talents * POUNDS_PER_TALENT * LOTS_PER_POUND
    + pounds * LOTS_PER_POUND
    + lots
)

# Total in grams
total_grams = total_lots * GRAMS_PER_LOT

# Total in kilograms and grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
