a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))
d = float(input("Enter value for d: "))

if c == d:
  print("Error: The denominator (c - d) is zero. Division by zero is not allowed.")
else:
  X = (a - b) / (c - d)
  print(f"The value of X is: {X}")