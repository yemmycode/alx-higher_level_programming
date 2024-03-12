#!/usr/bin/python3
import random
def classify_number(number):
if number > 0:
return "positive"
elif number == 0:
return "zero"
else:
return "negative"
number = random.randint(-10, 10)
result = classify_number(number)
print(f"{number} is {result}")
