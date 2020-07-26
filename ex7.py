#Company salary

year_employed = int(input("Years of employed: "))
number_of_kids = int(input("Number of kids: "))

minimum_wage = 400

total_kids = number_of_kids * 30
total_years = year_employed * 20
total = minimum_wage + total_kids + total_years

print("The total amount is " + str(total) + "$. " + str(minimum_wage) + "$ minimum wage + " + str(total_years) + "$ for " + str(year_employed) + " years expiriance + " + str(total_kids) + "$ for " + str(number_of_kids) + " kids.")
