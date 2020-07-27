from math import *
#Calculating range until inputed number

num = int(input("Input a number: "))
sum = 0
for i in range(num+1):
    sum = sum + i
print("The sum is ", sum)