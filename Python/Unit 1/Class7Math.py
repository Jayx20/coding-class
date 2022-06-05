import math
import random

# value = float(input('Give degrees: '))
# integer = math.radians(value)
# print(integer)

counter_zero = 0
counter_one  = 0
counter_two  = 0

for x in range(1000000):
    val = random.randint(0, 2)

    if val == 0:
        counter_zero += 1
    elif val == 1:
        counter_one += 1
    elif val == 2:
        counter_two += 1

print('Zero:', counter_zero)
print('One:', counter_one)
print('Two:', counter_two)