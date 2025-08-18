a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
m = float(input("Enter value for m: "))
c = float(input("Enter value for c: "))
d = float(input("Enter value for d: "))
n = float(input("Enter value for n: "))

denominator = (a * d) - (c * b)

if denominator == 0:
  print("The denominator (ad - cb) is zero. The set of linear equations has no unique solution.")
else:
  x1 = ((m * d) - (b * n)) / denominator
  x2 = ((n * a) - (m * c)) / denominator
  print(f"The unique solutions are: x1 = {x1:.2f} and x2 = {x2:.2f}")