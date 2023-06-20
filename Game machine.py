import random

a = 0
b = 9
digits = []

for _ in range(16):
    digit = random.randint(a, b)
    digits.append(digit)

print(*digits)
