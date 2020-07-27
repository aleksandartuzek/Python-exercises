from math import *
#Positive or negative

print("Enter 5 numbers:")

numbers = []

for i in range(5):
    num = int(input())
    numbers.append(num)
for i in range(5):
    if numbers[i] > 0:
        print("Positive")
    else:
        print("Negative")