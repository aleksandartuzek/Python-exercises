#Percentage increase or decrease of value

coin_value = int(input("Coin value: "))
coin_increase = int(input("Coin incerase precetange: "))
total_coin_value = coin_value + (coin_value * coin_increase)/100
coin_increase_value = total_coin_value - coin_value

print("Total coin value: " + str(total_coin_value) + " .Increase value: " + str(coin_increase_value))