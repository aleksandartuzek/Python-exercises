from math import *
#Calculating average in range

num = int(input("Input a number: "))
sum = 0
for i in range(num+1):
    sum = sum + i
average = sum/num
average = round(average, 1)
print("The average is ", average)