from math import *
#How many things you can buy



hours_of_work = int(input("How many hours you worked: "))
hourly_income = int(input("Hourly income: "))
wage = hours_of_work * hourly_income

ps4_price = 200
samsung_phone_price = 900
tv_price = 500
game_skin_price = 9.99

ps4 = wage / ps4_price
samung_phone = wage / samsung_phone_price
tv = wage / tv_price
game_skin = wage / game_skin_price

print ("I can buy " + str(floor(ps4)) + " PS4, " + str(floor(samung_phone)) + " Samsung, " + str(floor(tv)) + " TV," +  str(floor(game_skin)) +" game skin")
