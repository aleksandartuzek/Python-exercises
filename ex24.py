#Flip a coin

print("Flip a coin: ")

flip = str
sum_head = 0
sum_tail = 0

while flip != "stop":
    flip = input()
    if flip == 'head':
        sum_head = sum_head + 1
    elif flip == 'tail':
        sum_tail = sum_tail + 1

print("The end!")
print("Head won", sum_head, "times and tail won", sum_tail, "times.")

head_percent = 100*(sum_head/(sum_head+sum_tail))
tail_percent = 100 - head_percent
print("Head", head_percent,"%, Tail", tail_percent, "%.")