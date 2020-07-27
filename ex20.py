from math import *
#Calculating average of five numbers

print("Enter 5 numbers: ")
sum = 0
for i in range(5):
    num = int(input())
    sum = sum + num
average = sum/5
average = round(average, 2)
print("The average is :", average)