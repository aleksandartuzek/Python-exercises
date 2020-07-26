#Internet cafe charging

hours = int(input("Input hours: "))
user_member = True
user = True
user_member_price = 2
user_price = 5
total_member = user_member_price * hours
total_user = user_price * hours
tax_member = (total_member + (user_member_price * hours)*0.10)
tax_user = (total_user + (user_price * hours) * 0.20)
total = tax_member
total_tax_user = tax_user
if user_member:
    print("The user is a member stayed " + str(hours) + " hours for 2$/hour plus the 10% the total amount is " + str(total) +"$" )
else:
    print("")

if user:
    print("The user is not a member stayed " + str(hours) + " hours for 5$/hour plus the 20% the total amount is " + str(total_tax_user) +"$" )
else:
    print("")