#Salaries in company

salaries = []
employees = []
employee_num = 0
while employee_num >=0:
    name = input("Enter employee name: ")
    employees.append(name)
    salary = int(input("Enter salary: "))
    salaries.append(salary)
    more = input("Conitnue? (yes/no) ")
    if more == "no":
        break
max_salary = salaries[0]

for i in range(1, len(salaries)):
    if salaries[i] > max_salary:
        max_salary = salaries[i]
        print(employees[i], "-", max_salary)
    else:
       print("")