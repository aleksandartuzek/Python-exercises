#A cell phone company

call_duration = int(input("Input call duration:  "))

if call_duration <= 500:
    price = call_duration*0.01
elif 501 <= call_duration <=800:
    price = 500*0.01 + (call_duration-500)*0.008
else:
    price = 500*0.01 + 300*0.008 + (call_duration-800)*0.005

print("Total amount: ", price, "$.")