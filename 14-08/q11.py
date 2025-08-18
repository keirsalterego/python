num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
choice = input("Enter the operation (+, -, *, /): ")

if choice == '+':
  result = num1 + num2
  print(f"{num1} + {num2} = {result}")
elif choice == '-':
  result = num1 - num2
  print(f"{num1} - {num2} = {result}")
elif choice == '*':
  result = num1 * num2
  print(f"{num1} * {num2} = {result}")
elif choice == '/':
  if num2 == 0:
    print("Error: Division by zero is not allowed.")
  else:
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
  print("Invalid operation choice.")