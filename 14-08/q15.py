weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
  print("Classification: Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
  print("Classification: Normal weight")
elif bmi >= 25.0 and bmi <= 29.9:
  print("Classification: Overweight")
else:
  print("Classification: Obese")