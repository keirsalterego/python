age = int(input("Enter your age: "))

if age >= 60:
  print("Category: Senior Citizen")
elif age >= 20:
  print("Category: Adult")
elif age >= 13:
  print("Category: Teenager")
elif age >= 0:
  print("Category: Child")
else:
  print("Age cannot be negative.")