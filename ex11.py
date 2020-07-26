#Calculates the total consumption

wikipedia_mb_consupmtion = int(input("Input Wikipedia Mb consupmtion: "))
meme_mb_consupmtion = int(input("Input Meme Mb consupmtion: "))

wikipedia_mb_cost = wikipedia_mb_consupmtion + 0.10
meme_mb_cost = meme_mb_consupmtion + 0.05

total = meme_mb_cost + wikipedia_mb_cost

if total > 100:
    print("Total consumption is greater than 100$")
else:
    print("Your consumption is " +str(total) + "$.")

if meme_mb_consupmtion > wikipedia_mb_consupmtion:
    print("WOW MANY MEMES")
else:
    print("")