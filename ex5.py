#Amount of items you can buy

money = int(input("Input amount of money: "))
bitcoin_price = 50
ethereum_price = 25
litecoin_price = 10
bitcoin = money / bitcoin_price
ethereum = money / ethereum_price
litecoin = money / litecoin_price

print("With " + str(money) + "$, you can buy: " + str(bitcoin) + " Bitcoins, " + str(ethereum) + " Ethereum, and " + str(litecoin) + " Litecoins.")