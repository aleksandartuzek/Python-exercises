#Price with tax percentage

laptop_price = int(input("Input laptop price: "))
tax_percentage = int(input("Input tax percentage: "))
total = laptop_price + (laptop_price * tax_percentage)/100

print("Total price of the laptop is: " + str(total) + "$")