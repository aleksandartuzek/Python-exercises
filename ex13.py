#Calculating shipping cost

product_price = int(input("Input product price : "))
location = input("Input your destination (US, Europe, Canada, Other): ")

antartic = 11
us = 5
europe = 7
canada = 3
other = 9

total_us = product_price + us
total_europe = product_price + europe
total_canada = product_price + canada
total_other = product_price + other

if location == "US":
    print("You have to pay " + str(total_us) + "$," + str(product_price) + "$ for the product and " + str(us) + "$ for shipping cost.")
elif location == "Europe":
    print("You have to pay " + str(total_europe) + "$," + str(product_price) + "$ for the product and " + str(europe) + "$ for shipping cost.")
elif location == "Canada":
    print("You have to pay " + str(total_canada) + "$," + str(product_price) + "$ for the product and " + str(canada) + "$ for shipping cost.")
else:
    print("You have to pay " + str(total_other) + "$," + str(product_price) + "$ for the product and " + str(other) + "$ for shipping cost." )

