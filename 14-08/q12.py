marks1 = float(input("Enter marks for subject 1 (out of 100): "))
marks2 = float(input("Enter marks for subject 2 (out of 100): "))
marks3 = float(input("Enter marks for subject 3 (out of 100): "))

average_marks = (marks1 + marks2 + marks3) / 3

if average_marks >= 90:
  print("Grade: A")
elif average_marks >= 80:
  print("Grade: B")
elif average_marks >= 70:
  print("Grade: C")
elif average_marks >= 60:
  print("Grade: D")
else:
  print("Grade: F")