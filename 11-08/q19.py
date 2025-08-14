basic_salary = float(input("Enter the basic salary: "))

da = basic_salary * 0.60
hra = basic_salary * 0.15

gross_salary = basic_salary + da + hra

print(gross_salary)