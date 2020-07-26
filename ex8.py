#Company salary with day off

year_employed = int(input("Years of employed: "))
number_of_kids = int(input("Number of kids: "))
missed_day = int(input("Number of missed days: "))

minimum_wage = 400
bonus = 100

total_kids = number_of_kids * 30
total_years = year_employed * 20
total = minimum_wage + total_kids + total_years

if missed_day == 0:
     print("The total amount is " + str(total) + "$. " + str(minimum_wage) + "$ minimum wage + " + str(total_years) + "$ for " + str(year_employed) + " years expiriance + " + str(total_kids) + "$ for " + str(number_of_kids) + " kids + " + str(bonus) + "$ fot not missing a day at work.")
else :
     print("The total amount is " + str(total) + "$. " + str(minimum_wage) + "$ minimum wage + " + str(total_years) + "$ for " + str(year_employed) + " years expiriance + " + str(total_kids) + "$ for " + str(number_of_kids) + " kids.")