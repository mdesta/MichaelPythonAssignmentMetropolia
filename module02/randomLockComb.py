
print("This program generates random lock combinations for locks with 3-digit and 4-digit codes.")
print("The 3-digit code uses digits from 0 to 9")
print("The 4-digit code uses digits from 1 to 6.")

import random

# SInce this is for a combination lock
# digits can/should repeat, e.g. 222 is OK
codeForThreeDigitLock = [random.randint(0, 9) for _ in range(3)]
codeForFourDigitLock = [random.randint(1, 6) for _ in range(4)]

print("3-digit combination (0–9):", "".join(map(str, codeForThreeDigitLock)))
print("4-digit combination (1–6):", "".join(map(str, codeForFourDigitLock)))