#Apartments price

apartments_price = 1
apartments = []
sum_apartments = 0

while apartments_price > 0:
    apartments_price = int(input("Apartment price: "))
    if apartments_price > 0:
        sum_apartments = sum_apartments + 1
        apartments.append(apartments_price)
        print("Apartment ", sum_apartments, "price: ", apartments_price)
    else:
        print("Now enter rent price. ")
        break

sum_price = 0
i = 0
for i in range(len(apartments)):
    sum_price = sum_price + apartments[i]
average = sum_price / sum_apartments
print(sum_apartments, "apartments have been registered. The average price for rent is", average)

price = 1
while price > 0:
    price = int(input("Rent price: "))
    if price > average:
        print("Above average price!")
    elif price == average:
        print("Same as average price!")
    elif 0 < price < average:
        print("Belove average price!")
    else:
        print("Quit!")