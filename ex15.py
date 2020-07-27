#A fast food chain menu

meal = input("Choose your meal: 1)Burger, 2)Pizza, 3)Hot Dog: ")

burger = 5
pizza = 3
hot_dog = 1.5

if meal == "Burger":
    print(meal + " " + str(burger) + "$.")
elif meal == "Pizza":
    print(meal + " " + str(pizza) + "$.")
elif meal == "Hot Dog":
    print(meal + " " + str(hot_dog) + "$.")
else:
    print("Your meal is not in menu!")