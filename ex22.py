from math import *
#Reads numbers and sum them until negative value

print("Input numbers:")

numbers = []
sum = 0

for i in range(10):
    num = int(input())
    if num < 0:
        break
    sum = sum + num

print("The sum is ", sum)