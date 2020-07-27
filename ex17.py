from math import *
#Calculating range (2, 4, 6...)

sum = 0
for i in range(102):
    if (i%2) == 1:
        sum = sum + i
print("The sum is ", sum)