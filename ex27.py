import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("Go!")

print("Enter the number of seconds:")
seconds = input()
while not seconds.isdigit():
    print("Thats not a number, enter a number:")
    seconds = input()
seconds = int(seconds)
countdown(seconds)