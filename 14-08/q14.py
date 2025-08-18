units = float(input("Enter the total units consumed: "))
bill = 0

if units <= 100:
  bill = units * 5
elif units > 100 and units <= 200:
  bill = (100 * 5) + ((units - 100) * 7)
else:
  bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print(f"Your total electricity bill is ₹{bill:.2f}.")