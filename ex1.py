#In this example, you will learn to swap two variables by using a temporary variable and without using temporary variable.

#1) Without temporary variable.

a = int(input("Input value of a: "))
b = int(input("Input value of b: "))

a = a + b
b = a - b
a = a - b

print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))

#2)With temporary variable.

a = int(input("Input value of a: "))
b = int(input("Input value of b: "))

temp = a
a = b
b = temp

print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))