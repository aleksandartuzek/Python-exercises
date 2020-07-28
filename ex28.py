#Garage company

drivers = 0
earnings = 0

while drivers >=0:
    member = input("Are you a member? (yes/no): ")
    if member == "yes":
        cost = 1.5
    elif member == "no":
        cost = 3


    hours = int(input("How many hours you have been parked?: "))
    if 0 < hours <= 1:
        hours_cost = 2
    elif 1 < hours <= 2:
        hours_cost = 3.5
    elif 2 < hours <= 3:
        hours_cost = 4.5
    else:
        hours_cost = 4.5 + (hours - 3)*0.5

    price = cost + hours_cost

    print("Total amount is: ", price, "$")

    drivers = drivers + 1
    earnings = earnings + price

    more = input("Do you want do continue? (yes/no)")
    if more == "no":
        print(drivers, "Driver payed. The total earnings are", earnings, "$")
        break